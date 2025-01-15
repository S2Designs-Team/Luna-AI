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

    def __init__(self):
        super().__init__()
        # Carica le impostazioni
        self.__loadSettings()
        # Inizializza tutti i componenti della finestra principale
        self.__initMainWindow()
        self.__initMainMenuBar()
        self.__initWorkArea()
        self.__initStatusBar()

        # Usa uno splitter per separare le sezioni con pannelli ridimensionabili
        self.splitter = QSplitter(Qt.Horizontal)
        # Configura proporzioni iniziali dello splitter
        self.splitter.setSizes([200, 700, 300])  # Dimensioni iniziali (Toolbox, Canvas, Pannello proprietà)
        self.main_layout.addWidget(self.splitter)        

        self.__initToolbox()
        self.__initCanvas()
        self.__initPropertyPanel()

    def __loadSettings(self):
        try:
            # Load settings
            self.__settings = self.__ConfigurationManager.loadYaml(self.__config_file_path)
        except Exception as e:
            print(f"Error loading the application settings: {e}")

    def __initMainWindow(self):
        try:
            self.objectName="MainWindow"
            # Apply settings to the main window
            self.setWindowTitle(self.__settings.getProperty("main_window.title"))  
            self.setGeometry(self.__settings.getProperty("main_window.top"), 
                             self.__settings.getProperty("main_window.left"), 
                             self.__settings.getProperty("main_window.width"),
                             self.__settings.getProperty("main_window.height"))    
        except Exception as e:
            print(f"Error MainWindow properties: {e}")
            # Opzionalmente, torna ai valori predefiniti
            self.setWindowTitle("[S2 Designs team] GUI Creator for python - Qt5 WYSIWYG")  
            self.setGeometry(0, 0, 800, 600)

    def __initMainMenuBar(self):
        self._MainMenuBar = MainMenuBar()
        # Inizializza la barra dei menu
        self.setMenuBar(self._MainMenuBar)

    def __initWorkArea(self):
        # Configura il layout principale
        self._WorkArea_container = QWidget()
        self.setCentralWidget(self._WorkArea_container)
        self.main_layout = QHBoxLayout()
        self._WorkArea_container.setLayout(self.main_layout)
        pass

    def __initToolbox(self):
        """Inizializza la Toolbox come un componente separato."""
        self.toolbox = ToolBox()
        self.splitter.addWidget(self.toolbox)

    def __initCanvas(self):
        """Inizializza il Canvas (area centrale per il design della GUI)."""
        self.canvas_frame = QWidget()
        self.canvas_frame.setStyleSheet("background-color: lightGray;")   
        self.canvas_frame.setAcceptDrops(True)

        # Aggiungi un componente contenitore window
        self.component_window = ResizableWidget(self.canvas_frame)
        self.component_window.setGeometry(0, 0, 600, 800)  # Imposta la dimensione e la posizione del contenitore
        self.component_window.setMinimumSize(QSize(600, 800))  # Imposta la dimensione minima
        self.component_window.setStyleSheet("""
            background-color: #FFD700;  /* Colore vivace */
            border: 2px solid black;  /* Bordo nero */
            border-radius: 10px;  /* Angoli arrotondati */
        """)
        self.component_window.mousePressEvent = self.onComponentWindowClick

        # Aggiungi un'ombra al componente window
        shadow_effect = QGraphicsDropShadowEffect(self.component_window)
        shadow_effect.setBlurRadius(15)
        shadow_effect.setOffset(5, 5)
        shadow_effect.setColor(QColor(0, 0, 0, 160))
        self.component_window.setGraphicsEffect(shadow_effect)

        # Aggiungi una barra del titolo alla finestra
        self.title_bar = QWidget(self.component_window)
        self.title_bar.setGeometry(0, 0, 600, 40)  # Aumenta l'altezza della barra del titolo
        self.title_bar.setStyleSheet("""
            background-color: #2E2E2E; 
            color: white; 
            border-top-left-radius: 10px; 
            border-top-right-radius: 10px;
            border-bottom-left-radius: 0px; 
            border-bottom-right-radius: 0px;
        """)
        self.title_layout = QHBoxLayout(self.title_bar)
        self.title_label = QLabel("Window Title", self.title_bar)
        self.title_layout.addWidget(self.title_label)
        self.title_layout.addStretch()
        self.close_button = QPushButton("X", self.title_bar)
        self.close_button.setFixedSize(30, 30)
        self.close_button.setStyleSheet("background-color: red; color: white; border: none;")
        self.title_layout.addWidget(self.close_button)

        # Zona di lavoro
        self.work_area = WorkArea(self.component_window)
        self.work_area.setGeometry(0, 40, 600, 760)  # Imposta la dimensione e la posizione della zona di lavoro
        self.work_area.setStyleSheet("""
            background-color: #FFFFFF; 
            border-top-left-radius: 0px; 
            border-top-right-radius: 0px;
            border-bottom-left-radius: 10px; 
            border-bottom-right-radius: 10px;
        """)
        self.work_area.mousePressEvent = self.onComponentWindowClick

        # Aggiungi la work_area al layout del component_window
        layout = QVBoxLayout(self.component_window)
        layout.addWidget(self.title_bar)
        layout.addWidget(self.work_area)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.component_window.setLayout(layout)

        self.splitter.addWidget(self.canvas_frame)

    def __initPropertyPanel(self):
        """Inizializza il Pannello delle proprietà (selezione degli attributi del componente)."""
        # Pannello delle proprietà
        self.properties_panel = PropertyPanel(self)
        self.splitter.addWidget(self.properties_panel)

    def __initStatusBar(self):
        """Inizializza la Status Bar."""
        self._MainStatusBar = MainStatusBar()
        self.setStatusBar(self._MainStatusBar)
        # Imposta un messaggio iniziale
        self._MainStatusBar.setMessage("Application ready")

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
            component_name = widget_under_cursor.objectName()
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


class WorkArea(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._designer_focused_component = None

    def setFocusedComponent(self, component):
        self._designer_focused_component = component
        self.update()  # Forza il ridisegno per richiamare paintEvent

    def paintEvent(self, event):
        """Disegna il bordo e i quadratini di ridimensionamento per il componente selezionato"""

        super().paintEvent(event)

        if self._designer_focused_component:
            painter = QPainter(self)
            if not painter.isActive():
                return
            pen = QPen(QColor(0, 0, 255), 2, Qt.SolidLine)
            painter.setPen(pen)
            rect = self._designer_focused_component.geometry()
            painter.drawRect(rect)

            # Disegna i quadratini di ridimensionamento
            handle_size = 6
            handles = [
                QPoint(rect.left(), rect.top()),
                QPoint(rect.right(), rect.top()),
                QPoint(rect.left(), rect.bottom()),
                QPoint(rect.right(), rect.bottom())
            ]
            for handle in handles:
                painter.fillRect(QRect(handle.x() - handle_size // 2, handle.y() - handle_size // 2, handle_size, handle_size), QColor(255, 0, 0))


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
