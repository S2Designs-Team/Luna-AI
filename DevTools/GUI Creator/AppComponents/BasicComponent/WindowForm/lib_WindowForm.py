import uuid
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QApplication)
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtGui import QPainter, QPen, QColor

from AppComponents.BasicComponent.Enums.lib_Enums import EnumLayout
from AppComponents.BasicComponent.Layout.lib_QFlowLayout import FlowLayout

class WindowForm(QWidget):

    __instanceHandleId:str      = None
    __layout_type:EnumLayout    = EnumLayout.VERTICAL
    __type:str                  = __build_class__.__name__
    __parent:any                = None

    #- [PROPERTIES]
    #--------------------------------------------------------------------------------------------
    @property
    def name(self):
        """
        Returns the name of the window form component. If the name is not set,
        it retrieves the type of the component and sets it as the name.

        Returns:
            str: The name of the window form component.
        """
        if not self.__name:
            self.__name= self.getType()
        return self.__name
    
    @property
    def layout_type(self):
        """
        Returns the layout type of the window form.

        :return: The layout type.
        :rtype: str
        """
        return self.__layout_type
    @layout_type.setter
    def layout_type(self, value:EnumLayout):
        """
        Sets the layout type for the window form.

        Args:
            value (EnumLayout): The layout type to be set.
        """
        self.__setLayoutType(value)
    
    #- [CLASS CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowFlags(Qt.SubWindow)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.component_window.setMinimumSize(QSize(480, 320))  # Imposta la dimensione minima
        self.__is_resizing     = False
        self.__resize_position = None
        self.initUI()
    
    #- [CLASS EVENTS]
    #--------------------------------------------------------------------------------------------
    def getType(self):
        """
        Retrieve the type of the component.

        Returns:
            str: The type of the component.
        """
        return self.__type
    
    def getHandle(self)->str:
        """
        Retrieve the handle ID of the window form instance.

        Returns:
            str: The handle ID of the window form instance.
        """
        return self.__instanceHandleId
    
    def getGraphDrawer(self):
        pass

    def initUI(self):
        self.__instanceHandleId = uuid.uuid4()
        self.__name             = "WindowForm"
        self.__setLayoutType(self.__layout_type)
        self.setStyleSheet("""
            WindowForm {
                background-color: #FFD700;  /* Colore vivace */
                border: 2px solid black;    /* Bordo nero */
                border-radius: 10px;        /* Angoli arrotondati */
            }
        """)
        self.__addTitleBarCtrl()

    def __

    #- [CLASS PRIVATE METHODS]
    #--------------------------------------------------------------------------------------------
    def __setLayoutType(self, par_layout_type: EnumLayout):
        """
        Sets the layout type for the window form.
        Args:
            par_layout_type (EnumLayout): The type of layout to set. Must be one of the following:
                - EnumLayout.VERTICAL: Sets a vertical box layout.
                - EnumLayout.HORIZONTAL: Sets a horizontal box layout.
                - EnumLayout.FLOW: Sets a flow layout.
        Raises:
            ValueError: If an invalid layout type is provided.
        """
        match par_layout_type:
            case EnumLayout.VERTICAL:
                self.layout = QVBoxLayout(self)
            case EnumLayout.HORIZONTAL:
                self.layout = QHBoxLayout(self)
            case EnumLayout.FLOW:
                self.layout = FlowLayout(self)
            case _:
                raise ValueError("Invalid layout type.")
        
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.layout)
        self.__layout_type = par_layout_type

    def __addTitleBarCtrl(self):
        self._component_title_bar = QWidget(self)
        self._component_title_bar.setFixedHeight(40)
        self._component_title_bar.setStyleSheet("""
            background-color: #2E2E2E; 
            color: white; 
            border-top-left-radius: 10px; 
            border-top-right-radius: 10px;
        """)

        title_layout = QHBoxLayout(self._component_title_bar)
        title_layout.setContentsMargins(5, 0, 5, 0)
        title_layout.setSpacing(5)

        self.title_label = QLabel("Window Title", self._component_title_bar)
        self.title_label.setStyleSheet("color: white;")
        title_layout.addWidget(self.title_label)

        title_layout.addStretch()

        self.component_titleBar_iconizer_button = QPushButton("-", self._component_title_bar)
        self.component_titleBar_iconizer_button.setFixedSize(30, 30)
        self.component_titleBar_iconizer_button.setStyleSheet("background-color: gray; color: white; border: none;")
        title_layout.addWidget(self.window_iconizer)

        self.window_expander = QPushButton("□", self._component_title_bar)
        self.window_expander.setFixedSize(30, 30)
        self.window_expander.setStyleSheet("background-color: gray; color: white; border: none;")
        title_layout.addWidget(self.window_expander)

        self.window_exiter = QPushButton("X", self._component_title_bar)
        self.window_exiter.setFixedSize(30, 30)
        self.window_exiter.setStyleSheet("background-color: red; color: white; border: none;")
        title_layout.addWidget(self.window_exiter)

        return self._component_title_bar