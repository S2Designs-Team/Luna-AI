
class Property:
    __name:str  = None
    __value:any = None

    @property
    def name(self):
        return self.__name
    
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        self.__value = value

    def __init__(self, par_name:str, type:any , par_default_value:any=None):
        if not par_name:
            raise RuntimeError("You must define a name for the property.")
        self.__name=par_name
