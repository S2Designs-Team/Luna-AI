from AppComponents.BasicComponent.lib_Property import Property

class GUIComponentSize():
    __width:Property  = Property("width",int, 100)
    __height:Property = Property("height",int, 60)

    __min_width:Property  = Property("min_width",int, 100)
    __min_height:Property = Property("min_height",int, 60)

    __max_width:Property  = Property("max_width",int, 200)
    __max_height:Property = Property("max_height",int, 120)

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value:int=0):
        self.__width = value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value:int=0):
        self.__height = value
        
    @property
    def min_width(self):
        return self.__min_width
    @min_width.setter
    def min_width(self, value:int=0):
        self.__min_width = value

    @property
    def min_height(self):
        return self.__min_height
    @min_height.setter
    def min_height(self, value:int=0):
        self.__min_height = value

    @property
    def max_width(self):
        return self.__max_width
    @max_width.setter
    def max_width(self, value:int=0):
        self.__max_width = value

    @property
    def max_height(self):
        return self.__max_height
    @max_height.setter
    def max_height(self, value:int=0):
        self.__max_height = value