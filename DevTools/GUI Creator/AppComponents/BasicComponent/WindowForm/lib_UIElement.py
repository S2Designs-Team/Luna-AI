import uuid
from abc                import ABCMeta, abstractmethod
from PyQt5.QtWidgets    import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QApplication)
from PyQt5.QtCore       import (Qt, QObject, QEvent, QSize, QPoint)
from .lib_EventsHandler import EventsHandler
from .lib_Position      import Position
from .lib_Size          import Size
from .lib_Border        import Border
from AppComponents.BasicComponent.Enums.lib_Enums          import EnumLayout
from AppComponents.BasicComponent.Layout.lib_QFlowLayout   import FlowLayout

# Creazione di una metaclasse composta
class QWidgetABCMeta(type(QWidget), ABCMeta):
    pass

class UIElement(QWidget, metaclass=QWidgetABCMeta):
    __instanceHandleId:str      = None
    __type:str                  = __build_class__.__name__
    __position:Position         = Position(0,0)
    __size:Size                 = Size(0,0)
    __borders:Border            = Border()
    __eventsHandler             = EventsHandler()
    __layout_type:EnumLayout    = EnumLayout.NONE
    __controls:dict             = {}

    #- [PROPERTIES]
    #--------------------------------------------------------------------------------------------
    @property
    def instanceHandle(self):
        return self.__instanceHandleId

    @property
    def eventsHandler(self):
        return self.__eventsHandler
    
    @property
    def name(self):
        """
        The name assigned to this component.
        """
        return self.objectName
    @name.setter
    def name(self, value:str):
        """
        Args:
            value (str): The component's name to be set.
        """
        self.objectName = value

    @property
    def top(self):
        """
        The top value of this component.
        """
        return self.__position.top
    @top.setter
    def top(self, value:int):
        """
        Args:
            value (int): The value to set as the top position.
        """
        self.setPosition(value, self.left)
        self.setGeometry(self.left, value, self.width, self.height)        
        self.update()
        self.repaint()

    @property
    def left(self):
        """
        The left value of this component.
        """
        return self.__position.left
    @left.setter
    def left(self, value:int):
        """
        Args:
            value (int): The new left value to be set.
        """
        self.setPosition(self.top, value)
        self.setGeometry(value, self.top, self.width, self.height)        
        self.update()
        self.repaint()

    @property
    def width(self):
        """
        The width value of this component.
        """
        return self.__size.width
    @width.setter
    def width(self, value:int):
        """
        Args:
            value (int): The width value to set.
        """
        self.setSize(value, self.height)
        self.setGeometry(self.left, self.top, value, self.height)
        self.update()
        self.repaint()

    @property
    def height(self):
        """
        The height value of this component.
        """
        return self.__size.height
    @height.setter
    def height(self, value:int):
        """
        Args:
            value (int): The height value to be set.
        """
        self.setSize(self.width, value)
        self.setGeometry(self.left, self.top, self.width, value)
        self.update()
        self.repaint()      

    @property
    def parent(self)->QWidget:
        """
        The parent container of this UI Element
        """
        try:
            return self.__parent
        except Exception as e:
            raise RuntimeError(f"[UIElement]::[parent]=>{e}")
    @parent.setter
    def parent(self, value:QWidget):
        """
        Args:
            value (int): The new parent container for this UI Element.
        """
        try:
            if not value:
                self.setParent(value)
        except Exception as e:
            raise RuntimeError(f"[UIElement]::[parent]=>{e}")

    @property
    def layout_type(self):
        return self.__layout_type
    @layout_type.setter
    def layout_type(self, value:EnumLayout):
        """
        Sets the layout type for the window form.

        Args:
            value (EnumLayout): The layout type to be set.
        """
        self.__setLayoutType(value)

    @property
    def controls(self):
        return self.__controls
    
    @property
    def css_style(self):
        """
        The CSS style string applied to the UI Element.
        """
        return self.styleSheet()
    @css_style.setter
    def css_style(self, value: str):
        """
        Args:
            value (str): The CSS style string to be applied.
        """
        try:
            object_selector = f"#{self.objectName}"  # Selector based on object name
            new_stylesheet = f"{object_selector} {{\n{value}\n}}"
            self.setStyleSheet(new_stylesheet)
            print(f"[{self.objectName}] Applied stylesheet:\n{new_stylesheet}")
            self.setVisible(True)
            self.update()
            self.repaint()
            self.show()            
        except Exception as e:
            raise RuntimeError(f"[UIElement]::[css_style] Error applying style: {e}")
    
    @property
    def borders(self):
        return self.__borders
    @borders.setter
    def borders(self, value:Border):
        self.__borders = value

    @property
    def background(self):
        return self.__background
    
    #- [CLASS CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------
    def __init__(self, par_parent:QObject=None):
        super().__init__(par_parent) if QObject else super().__init__()
        self.setParent(par_parent)
        self.__parent = par_parent
        self.objectName = "UIElement"
        self.__getUIElementInstanceHandleID()
        self.__getConcreteElementType()

    def addChild(self, par_ui_child_element:QObject):
        self.layout.addWidget(par_ui_child_element)
        self.__controls[par_ui_child_element.objectName] = par_ui_child_element

    def getType(self):
        """
        Retrieve the type of the UI Element.

        Returns:
            str: The type of the UI Element.
        """ 
        return self.__type
    
    def getHandle(self)->str:
        """
        Retrieve the handle ID of the UI Element instance.

        Returns:
            str: The handle ID of the UI Element instance.
        """
        return self.__instanceHandleId

    def setPosition(self, par_top:int=0, par_left:int=0):
        self.__position = Position(par_top, par_left)
        self.pos = QPoint(self.__position.top, self.__position.left)

    def setSize(self, par_width:int=0, par_height:int=0):
        self.__size = Size(par_width, par_height)
        self.setFixedSize(par_width, par_height)

    def mousePressEvent(self, event):
        self.eventsHandler.mousePressEvent(self, event)

    #- [CLASS PRIVATE METHODS]
    #--------------------------------------------------------------------------------------------
    def __getUIElementInstanceHandleID(self):
        try:
            self.__instanceHandleId = uuid.uuid4()  
        except Exception as e:
            raise RuntimeError(f"[UIElement]::[__getUIElementInstanceHandleID]=>{e}")

    def __getConcreteElementType(self):
        """
        Dynamically retrieve the type of the UI Element..
        """        
        my_class_class_name = self.__class__.__name__
        if not my_class_class_name:
            raise RuntimeError(f"[UIElement]::[__getConcreteElementType] => Unable to determine the type of the Concrete UI Element.")
        self.__type= my_class_class_name
        return self.__type

    def __setLayoutType(self, par_layout_type: EnumLayout):
        """
        Sets the layout type for this UI Element.\n
        Args:
            par_layout_type (EnumLayout): The type of layout to set.\n
            Must be one of the following:\n
            \t    - EnumLayout.VERTICAL: Sets a vertical box layout.
            \t    - EnumLayout.HORIZONTAL: Sets a horizontal box layout.
            \t    - EnumLayout.FLOW: Sets a flow layout.
        Raises:
            ValueError: If an invalid layout type is provided.
        """
        if self.layout() is not None:
            self.__clearCurrentLayout()

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
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)
        self.__layout_type = par_layout_type
        print(f"Layout type set to {par_layout_type} for {self.objectName}.")

    def __clearCurrentLayout(self):
        """
        Rimuove il layout corrente e tutti i suoi widget.
        """
        old_layout = self.layout()
        if old_layout is not None:
            while old_layout.count():
                child = old_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            del old_layout