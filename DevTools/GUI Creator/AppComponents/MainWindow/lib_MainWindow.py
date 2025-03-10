import os
from PyQt5.QtWidgets import (QPushButton, QApplication, QLabel, QListWidget, 
                             QMainWindow, QFrame, QMenuBar, QMenu, QAction, 
                             QToolBox, QVBoxLayout, QWidget, QHBoxLayout, 
                             QDockWidget, QSplitter, QGraphicsDropShadowEffect)
from PyQt5.QtCore import Qt, QPoint, QRect, QSize
from PyQt5.QtGui  import QPen, QColor, QPainter

from Helpers.ConfigurationManagement.lib_ConfigurationManager import ConfigurationManager
from Helpers.ComponentManagement.lib_ComponentManager         import ComponentManager
from ObjectsLib.ConfigDictionary.lib_ConfigDictionary         import ConfigDictionary
from AppComponents.MainMenu.lib_MainMenu                      import MainMenuBar
from AppComponents.MainStatusBar.lib_MainStatusBar            import MainStatusBar
from AppComponents.ToolBox.lib_ToolBox                        import ToolBox
from AppComponents.PropertyPanel.lib_PropertyPanel            import PropertyPanel
from AppComponents.BasicComponent.WindowForm.lib_WindowForm   import WindowForm
from AppComponents.BasicComponent.WindowForm.lib_UIElement    import UIElement
from AppComponents.BasicComponent.WindowForm.lib_Size         import Size

class MainWindow(QMainWindow):
 
    __settings:ConfigDictionary  = None
    __config_dir                 = "DevTools\\GUI Creator\\Config\\"
    __config_file_path           = os.path.join(__config_dir, "settings.yaml")
    __ConfigurationManager       = ConfigurationManager()
    __ComponentManager           = ComponentManager()
    __GuiControls                = []
    _MainMenuBar:MainMenuBar     = None
    _MainStatusBar:MainStatusBar = None
    _WorkArea_container:QWidget  = None
    _designer_focused_component  = None

    #- [CLASS CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__()
        # Load the settings
        self.__loadSettings()

        # Initialize all components of the main window.
        self.__initMainWindow()
        self.__initMainMenuBar()
        self.__initWorkArea()
        self.__initStatusBar()

        # Initialize all sub components in the WorkArea.
        self.__initToolbox()
        self.__initGuiDesignArea()
        self.__initPropertyPanel()

    #- [CLASS EXPOSED METHODS]
    #--------------------------------------------------------------------------------------------
    def update_status(self, message: str, timeout: int = 0):
        """Metodo per aggiornare la status bar."""
        self._MainStatusBar.setMessage(message, timeout)

    def createActionCall(self, par_action_name, method):
        status_action = QAction(par_action_name, self)
        status_action.triggered.connect(lambda: self.update_status("Status updated!", 3000))
        self.addAction(status_action)

    def mouseMoveEvent(self, event):
        """Cattura l'evento del movimento del mouse."""

        # Ottieni il componente sotto il cursore
        widget_under_cursor = self.childAt(event.pos())

        if widget_under_cursor:
            component_name = widget_under_cursor.objectName
            pos_x = event.x()
            pos_y = event.y()

            message = f"Component: {component_name}, Position: ({pos_x}, {pos_y})"
            # Aggiorna la StatusBar con il nome del componente e la posizione
            self._MainStatusBar.setMessage(message, 0)
        else:
            # Se non c'è nessun componente sotto il cursore, cancella il messaggio
            self._MainStatusBar.clearMessage()

    def onComponentWindowClick(self, event):
        """Gestisce il click sulla superficie del componente window"""
        component = self.toolbox.getSelectedComponent()
        if component:
            self.createComponent(component, event.pos().x(), event.pos().y())
            self.toolbox.clearSelectedComponent()
            self.properties_panel.updateProperties(component)

    def createComponent(self, component, x, y):
        """Crea un nuovo componente nella superficie del componente window"""
        component.setParent(self.work_area)
        component.text = "Label di prova"
        component.move(x, y)
        component.show()
        component.mousePressEvent = lambda event, comp=component: self.onDesignerComponentClick(event, comp)        
        return component
    
    def onDesignerComponentClick(self, event, component):
        """Gestisce il click su un componente nella superficie del componente window"""
        self._designer_focused_component = component
        self.properties_panel.updateProperties(component)
        self.work_area.setFocusedComponent(component)  # Forza il ridisegno per richiamare paintEvent

    #- [CLASS PRIVATE METHODS]
    #--------------------------------------------------------------------------------------------
    def __loadSettings(self):
        try:
            # Load settings
            self.__settings = self.__ConfigurationManager.loadYaml(self.__config_file_path)
        except Exception as e:
            print(f"Error loading the application settings: {e}")

    def __initMainWindow(self):
        try:
            self.objectName="MainWindow"
            # Property to distinguish the design mode
            self.isDesignerWindow = True            
            # Apply settings to the main window
            self.setWindowTitle(self.__settings.getProperty("main_window.title"))  
            self.setGeometry(self.__settings.getProperty("main_window.top"), 
                             self.__settings.getProperty("main_window.left"), 
                             self.__settings.getProperty("main_window.width"),
                             self.__settings.getProperty("main_window.height"))    
        except Exception as e:
            print(f"Error MainWindow properties: {e}")
            # Optionally, revert to default values
            self.setWindowTitle("[S2 Designs team] GUI Creator for python - Qt5 WYSIWYG")  
            self.setGeometry(0, 0, 800, 600)

    def __initMainMenuBar(self):
        self._MainMenuBar = MainMenuBar()
        # Initialize the menu bar
        self.setMenuBar(self._MainMenuBar)

    def __initWorkArea(self):
        """
        Initialize the Designer application Work Area as a separate component.
        """
        # Configure the main layout
        self._WorkArea_container = QWidget()
        self.setCentralWidget(self._WorkArea_container)
        self.main_layout = QHBoxLayout()
        self._WorkArea_container.setLayout(self.main_layout)

        # Use a splitter to separate sections with resizable panels.
        self.splitter = QSplitter(Qt.Horizontal)
        # Set the initial proportions of the splitter
        self.splitter.setSizes([200, 700, 300])  # Initial sizes (Toolbox, Canvas, Properties Panel)
        self.main_layout.addWidget(self.splitter) 

        pass

    def __initToolbox(self):
        """
        Initialize the Toolbox as a separate component.
        """
        self.toolbox = ToolBox()
        self.splitter.addWidget(self.toolbox)

    def __initGuiDesignArea(self):
        """
        Initialize the Design Area (central area for GUI design).
        """
        self.gui_design_area = QFrame()
        self.gui_design_area.setStyleSheet("background-color: lightGrey;")
        self.gui_design_area.setAcceptDrops(False)
        layout = QVBoxLayout(self.gui_design_area)

        # Add a WindowForm container component  
        self.designer_window = WindowForm(self.gui_design_area)
        print(f"WindowForm Ctrl Name : {self.designer_window.name}")
        print(f"           Ctrl type : {self.designer_window.getType()}")
        print(f"           Handle ID : {self.designer_window.getHandle()}")
        print(f"           Parent    : {self.designer_window.parent.objectName()}")
        print(f"           Size      : w:{self.designer_window.size().width()}, h:{self.designer_window.size().height()}")

        # Aggiungi un'ombra al componente window
        shadow_effect = QGraphicsDropShadowEffect(self.designer_window)
        shadow_effect.setBlurRadius(15)
        shadow_effect.setOffset(5, 5)
        shadow_effect.setColor(QColor(0, 0, 0, 160))

        self.designer_window.setGraphicsEffect(shadow_effect)
        layout.addWidget(self.designer_window)
        layout.setContentsMargins(0, 0, 0, 0)  # Rimuovi margini

        self.gui_design_area.setLayout(layout)
        self.splitter.addWidget(self.gui_design_area)


        # # Zona di lavoro
        # self.work_area = WorkArea(self.designer_window)
        # self.work_area.setGeometry(0, 40, 600, 760)  # Imposta la dimensione e la posizione della zona di lavoro
        # self.work_area.setStyleSheet("""
        #     background-color: #FFFFFF; 
        #     border-top-left-radius: 0px; 
        #     border-top-right-radius: 0px;
        #     border-bottom-left-radius: 10px; 
        #     border-bottom-right-radius: 10px;
        # """)
        # self.work_area.mousePressEvent = self.onComponentWindowClick

        # # Aggiungi la work_area al layout del component_window
        # layout = QVBoxLayout(self.designer_window)
        # layout.addWidget(self.title_bar)
        # layout.addWidget(self.work_area)
        # layout.setContentsMargins(0, 0, 0, 0)
        # layout.setSpacing(0)
        # self.designer_window.setLayout(layout)

    def __initPropertyPanel(self):
        """
        Initialize the Properties Panel (component attributes selection).
        """
        # Properties Panel
        self.properties_panel = PropertyPanel(self)
        self.splitter.addWidget(self.properties_panel)

    def __initStatusBar(self):
        """Inizializza la Status Bar."""
        self._MainStatusBar = MainStatusBar()
        self.setStatusBar(self._MainStatusBar)
        # Imposta un messaggio iniziale
        self._MainStatusBar.setMessage("Application ready")



class ResizableWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.setWindowFlags(Qt.SubWindow)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("""
            background-color: #FFD700;  /* Colore vivace */
            border: 2px solid black;  /* Bordo nero */
            border-radius: 10px;  /* Angoli arrotondati */
        """)

        self._is_resizing = False
        self._resize_position = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self._is_in_resize_area(event.pos()):
                self._is_resizing = True
                self._resize_position = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._is_resizing:
            delta = event.globalPos() - self._resize_position
            new_width = self.width() + delta.x()
            new_height = self.height() + delta.y()
            self.setFixedSize(new_width, new_height)
            self._resize_position = event.globalPos()
        else:
            if self._is_in_resize_area(event.pos()):
                self.setCursor(Qt.SizeFDiagCursor)
            else:
                self.setCursor(Qt.ArrowCursor)
        event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_resizing = False
            event.accept()

    def _is_in_resize_area(self, pos):
        return pos.x() > self.width() - 10 and pos.y() > self.height() - 10
