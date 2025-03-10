
class Size():

    __width:int         = 0
    __height:int        = 0

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value:int):
        self.__width = value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value:int):
        self.__height = value

    def __init__(self, par_width:int=0, par_height:int=0):
        self.__width = par_width
        self.__height= par_height
