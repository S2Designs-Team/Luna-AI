from lib_Property import Property

class GUIComponentPosition():
    __top:Property  = Property("top",int, 0)
    __left:Property = Property("left",int, 0)

    @property
    def top(self):
        return self.__top
    @top.setter
    def top(self, value:int=0):
        self.__top = value

    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self, value:int=0):
        self.__left = value
        
