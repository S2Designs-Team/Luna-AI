from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, pyqtProperty, QPoint
from .lib_Border   import Border
from .lib_Position import Position

class BasicUIControl(QWidget):
    __instanceHandleId:str      = None
    __name:str                  = "BasicUIControl"
    __type:str                  = __build_class__.__name__
    __position:Position         = Position()
    __width_value:int           = 100
    __height_value:int          = 100
    __borders:Border            = None

    #- [PROPERTIES]
    #--------------------------------------------------------------------------------------------
    @property
    def title(self):
        """
        The title text of the window form.
        """
        return self.__title_text
    @title.setter
    def title(self, value:str):
        """
        Args:
            value (str): The title text to be set.
        """
        self.__title_text = value

    @property
    def position(self)->Position:
        return self.__position
    @position.setter
    def position(self, value:Position):
        self.__position = value

    @property
    def width(self):
        """
        The width value of the title bar.
        """
        return self.__width_value
    @width.setter
    def width(self, value:int):
        """
        Args:
            value (int): The width value to set.
        """
        self.__width_value = value

    @property
    def height(self):
        """
        The height value of the title bar.
        """
        return self.__height_value
    @height.setter
    def height(self, value:int):
        """
        Args:
            value (int): The height value to be set.
        """
        self.__height_value = value
    
    @property
    def borders(self):
        return self.__borders
    @borders.setter
    def borders(self, value:Border):
        self.__borders = value

    @property
    def background(self):
        return self.__background
    

class TitleBar(QWidget):
    __instanceHandleId:str      = None
    __name:str                  = "Titlebar"
    __type:str                  = __build_class__.__name__    
    __title_text:str            = None
    
    __top_value:int             = 0
    __left_value:int            = 0
    __width_value:int           = 100
    __height_value:int          = 100
    __border:Border             = Border.

    #- [PROPERTIES]
    #--------------------------------------------------------------------------------------------
    @property
    def title(self):
        """
        The title text of the window form.
        """
        return self.__title_text
    @title.setter
    def title(self, value:str):
        """
        Args:
            value (str): The title text to be set.
        """
        self.__title_text = value

    @property
    def top(self):
        """
        The top value of the window form.
        """
        return self.__top_value
    @top.setter
    def top(self, value):
        """
        Args:
            value (int): The value to set as the top position.
        """
        self.__top_value = value

    @property
    def left(self):
        """
        The left value of the title bar.
        """
        return self.__left_value
    @left.setter
    def left(self, value):
        """
        Args:
            value (int): The new left value to be set.
        """
        self.__left_value

    @property
    def width(self):
        """
        The width value of the title bar.
        """
        return self.__width_value
    @width.setter
    def width(self, value:int):
        """
        Args:
            value (int): The width value to set.
        """
        self.__width_value = value

    @property
    def height(self):
        """
        The height value of the title bar.
        """
        return self.__height_value
    @height.setter
    def height(self, value:int):
        """
        Args:
            value (int): The height value to be set.
        """
        self.__height_value = value
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self._is_dragging = False
        self._drag_position = None

        self.initUI()

    def initUI(self):
        self.setFixedHeight(40)
        self.setStyleSheet("""
            background-color: #2E2E2E; 
            color: white; 
            border-top-left-radius: 10px; 
            border-top-right-radius: 10px;
        """)

        self.title_layout = QHBoxLayout(self)
        self.title_layout.setContentsMargins(5, 0, 5, 0)
        self.title_layout.setSpacing(5)

        self.title_label = QLabel("Window Title", self)
        self.title_label.setStyleSheet("color: white;")
        self.title_layout.addWidget(self.title_label)

        self.title_layout.addStretch()

        self.window_iconizer = QPushButton("-", self)
        self.window_iconizer.setFixedSize(30, 30)
        self.window_iconizer.setStyleSheet("background-color: gray; color: white; border: none;")
        self.title_layout.addWidget(self.window_iconizer)

        self.window_expander = QPushButton("□", self)
        self.window_expander.setFixedSize(30, 30)
        self.window_expander.setStyleSheet("background-color: gray; color: white; border: none;")
        self.title_layout.addWidget(self.window_expander)

        self.window_exiter = QPushButton("X", self)
        self.window_exiter.setFixedSize(30, 30)
        self.window_exiter.setStyleSheet("background-color: red; color: white; border: none;")
        self.title_layout.addWidget(self.window_exiter)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = True
            self._drag_position = event.globalPos() - self._parent.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._is_dragging:
            self._parent.move(event.globalPos() - self._drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = False
            event.accept()

    def getTitle(self):
        return self.title_label.text()

    def setTitle(self, title):
        self.title_label.setText(title)

    Title = pyqtProperty(str, getTitle, setTitle)