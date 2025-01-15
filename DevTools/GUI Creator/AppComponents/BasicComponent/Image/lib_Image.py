from PyQt5.QtGui                           import QPixmap, QPainter
from AppComponents.BasicComponent.lib_Size import GUIComponentSize

class Image():

    __name:str              = None
    __size:GUIComponentSize = GUIComponentSize()
    __image:str             = None

    @property
    def image(self)->str:
        return self.__image
    @image.setter
    def image(self, value):
        self.__image = value
        self.setPicture(QPixmap(self.image))

    def __init__(self, parent=None):
        pass