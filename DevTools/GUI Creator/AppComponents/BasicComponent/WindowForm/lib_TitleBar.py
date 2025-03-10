from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore    import Qt, pyqtProperty, QPoint
from .lib_UIElement  import UIElement
from AppComponents.BasicComponent.Enums.lib_Enums          import EnumLayout

class TitleBar(UIElement):
    #- [PROPERTIES]
    #--------------------------------------------------------------------------------------------
    @property
    def title(self):
        """
        The title text of the window form.
        """
        return self.LBL_Title.text
    @title.setter
    def title(self, value:str):
        """
        Args:
            value (str): The title text to be set.
        """
        self.titleCaption_ctrl.setText(value)
        self.titleCaption_ctrl.update()
    
    #- [CLASS CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------
    def __init__(self, par_parent:QWidget=None):
        super().__init__(par_parent)
        self.objectName      = "TitleBar"
        self.layout_type     = EnumLayout.HORIZONTAL
        self.setPosition(0, 0)
        self.setSize(par_parent.width, 40)
        self._is_dragging   = False
        self._drag_position = None
        #self.css_style = f"""
        #    background-color:           #2E2E2E; 
        #    border:                     1px solid black;
        #    border-top-left-radius:     10px;
        #    border-top-right-radius:    10px;
        #    border-bottom-left-radius:  0px; 
        #    border-bottom-right-radius: 0px;
        #"""
        self.titleCaption_ctrl   = self.__createTitleCaption()
        self.iconizerButton_ctrl = self.__createIconizerButton()
        self.expanderButton_ctrl = self.__createExpanderButton()
        self.exiterButton_ctrl   = self.__createExiterButton()

        self.addChild(self.titleCaption_ctrl)
        self.layout.addStretch()
        self.addChild(self.iconizerButton_ctrl)
        self.addChild(self.expanderButton_ctrl)
        self.addChild(self.exiterButton_ctrl)

        self.__setEventsCallbacks()
 

    #- [CLASS PRIVATE METHODS]
    #--------------------------------------------------------------------------------------------
    def __createTitleCaption(self):
        my_new_ctrl            = QLabel()
        my_new_ctrl.objectName = "LBL_Title"
        my_new_ctrl.setText("Default title")
        my_new_ctrl.setFixedSize(self.width, 30)
        my_new_ctrl.setStyleSheet(f"""
            color:            #FFD700;
            background-color: transparent;   
            border-radius:    10px;
        """)
        return my_new_ctrl

    def __createIconizerButton(self):
        my_new_ctrl = QPushButton("-", self)
        my_new_ctrl.setFixedSize(24, 24)
        my_new_ctrl.setStyleSheet("background-color: gray; color: white; border: none; border-radius: 12px;")
        return my_new_ctrl

    def __createExpanderButton(self):
        my_new_ctrl = QPushButton("□", self)
        my_new_ctrl.setFixedSize(24, 24)
        my_new_ctrl.setStyleSheet("background-color: gray; color: white; border: none; border-radius: 12px;")
        return my_new_ctrl

    def __createExiterButton(self):
        my_new_ctrl = QPushButton("X", self)
        my_new_ctrl.setFixedSize(24, 24)
        my_new_ctrl.setStyleSheet("background-color: red; color: white; border: none; border-radius: 12px;")
        return my_new_ctrl

    def __setEventsCallbacks(self):
        self.eventsHandler.setOnMouseClick_delegate(self.onMouseClick)
        self.eventsHandler.setOnMouseHover_delegate(self.onMouseMoveOver)

    #- [CLASS EVENTS]
    #--------------------------------------------------------------------------------------------
    def onMouseClick(self, sender, event):
        print(f"[{self.objectName}] Handles the click on the UI element surface")
        self.title="Title bar clicked. Title Caption changed."
        pass
        
    def getGraphDrawer(self):
        pass

    """
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = True
            self._drag_position = event.globalPos() - self.__parent.frameGeometry().topLeft()
            event.accept()
    """

    def onMouseMoveOver(self, sender, event):
        if self._is_dragging:
            self._parent.move(event.globalPos() - self._drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = False
            event.accept()
    