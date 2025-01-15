from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout, QApplication
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt, QByteArray, pyqtSignal, QEvent, QSize, QPoint
from AppComponents.BasicComponent.lib_Size import GUIComponentSize
from AppComponents.BasicComponent.Enums.lib_Enums import EnumLayout
from AppComponents.BasicComponent.Layout.lib_QFlowLayout import FlowLayout

class IconButton(QWidget):
    mouseOver  = pyqtSignal()
    mouseClick = pyqtSignal()
    startDrag  = pyqtSignal()
    stopDrag   = pyqtSignal()

    _drag_start_position:QPoint = None
    __name:str                  = None
    __type:str                  = __build_class__.__name__
    __image_path:str            = None
    __text:str                  = None
    __layout_type:EnumLayout    = EnumLayout.VERTICAL
    __is_border_visible:bool    = False
    __border_radius:int         = 10
    __image_ctrl:QLabel         = None
    __text_ctrl:QLabel          = None

    #- [PROPERTIES]
    #--------------------------------------------------------------------------------------------
    @property
    def name(self):
        if not self.__name:
            self.__name= self.getType()
        return self.__name

    @property
    def image_path(self):
        return self.__image_path
    @image_path.setter
    def image_path(self, value):
        self.__setIconImage(value)

    @property
    def text(self):
        return self.__text
    @text.setter
    def text(self, value: str):
        self.__changeText(value)

    @property
    def border_radius(self):
        return self.__border_radius
    @border_radius.setter
    def border_radius(self, value:int):
        self.__border_radius = value
    
    @property
    def layout_type(self):
        return self.__layout_type
    @layout_type.setter
    def layout_type(self, value:EnumLayout):
        self.__setLayoutType(value)
    
    #- [CLASS CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------
    def __init__(self, par_res_picture_path:str = None, par_button_text:str = "Default text"):
        super().__init__()
        self.__name = "IconButton"
        self.__setLayoutType(self.__layout_type)
        self.__addIconImageCtrl()
        self.__addTextLabelCtrl(par_button_text)
        self.__setIconImage(par_res_picture_path)
        self.setMouseTracking(True)
        self.setFixedSize(100, 100)
    
    #- [CLASS EVENTS]
    #--------------------------------------------------------------------------------------------
    def enterEvent(self, event):
        self.mouseOver.emit()
        self.__is_border_visible = True
        self.update()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.__is_border_visible = False
        self.update()
        super().leaveEvent(event)

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.__is_border_visible:
            painter = QPainter(self)
            pen     = QPen(Qt.black, 1)
            painter.setPen(pen)
            if self.border_radius > 0:
                painter.drawRoundedRect(0, 0, self.width() - 1, self.height() - 1, self.border_radius, self.border_radius)
            else:
                painter.drawRect(0, 0, self.width() - 1, self.height() - 1)
 
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouseClick.emit()
            self._drag_start_position = event.pos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            if self._drag_start_position is not None and (event.pos() - self._drag_start_position).manhattanLength() > QApplication.startDragDistance():
                self.startDrag.emit()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.stopDrag.emit()
            self.mouseClick.emit()
        super().mouseReleaseEvent(event) 
    
    #- [CLASS EXPOSED METHODS]
    #--------------------------------------------------------------------------------------------
    def getType(self):
        return self.__type

    #- [CLASS PRIVATE METHODS]
    #--------------------------------------------------------------------------------------------
    def __addIconImageCtrl(self):
        self.__image_ctrl = QLabel(self)
        self.__image_ctrl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.__image_ctrl)

    def __addTextLabelCtrl(self, text: str = ""):
        self.__text_ctrl = QLabel(text, self)
        self.__text_ctrl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.__text_ctrl)

    def __setIconImage(self, par_new_image_path: str = None):
        if par_new_image_path:
            my_image = QPixmap(par_new_image_path)
            if my_image.isNull():
                print(f"Image not found: {par_new_image_path}. Using default image.")
                my_image = self.__getDefaultIconImage()
                self.__image_path = "Default"
            else:
                self.__image_path = par_new_image_path
        else:
            my_image = self.__getDefaultIconImage()
            self.__image_path = "Default"

        self.__updateIconImageSize(my_image, QSize(32, 32))

    def __updateIconImageSize(self, my_image: QPixmap, size: QSize = None):
        if size is None:
            size = self.size()
        my_image = my_image.scaled(size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.__image_ctrl.setPixmap(my_image)
        self.update()

    def __changeText(self, par_new_text: str):
        if par_new_text:
            self.__text_ctrl.setText(par_new_text)
        else:
            self.__text_ctrl.hide()

    def __getDefaultIconImage(self):
        try:
            my_image_manager = QPixmap()
            my_default_image_path = "DevTools\\GUI Creator\\Resources\\image.png"
            my_image_manager.load(my_default_image_path)
            return my_image_manager
        except Exception as e:
            raise RuntimeWarning(f"Default image could not be loaded: {e}")

    def __setLayoutType(self, par_layout_type: EnumLayout):
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