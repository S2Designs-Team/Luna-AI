class Position():

    __top:int         = 0
    __left:int        = 0

    @property
    def top(self):
        return self.__top
    @top.setter
    def top(self, value:int):
        self.__top = value

    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self, value:int):
        self.__left = value

    def __init__(self, par_top:int=0, par_left:int=0):
        self.__top = par_top
        self.__left= par_left
