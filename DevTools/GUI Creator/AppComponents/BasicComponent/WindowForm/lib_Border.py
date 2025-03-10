from PyQt5.QtGui                                  import (QColor)
from AppComponents.BasicComponent.Enums.lib_Enums import (EnumSides, EnumCorners)

class Border():
    __top_thickness:int       = 1
    __left_thickness:int      = 1
    __right_thickness:int     = 1
    __bottom_thickness:int    = 1

    __top_left_radius:int     = 1
    __top_right_radius:int    = 1
    __bottom_right_radius:int = 1
    __bottom_left_radius:int  = 1

    __color:QColor            = QColor(0, 0, 0)  # Black
    
    @property
    def thickness(self, par_side_filter:EnumSides=EnumSides.ALL_SIDES):
        my_sides_map = {
            EnumSides.UP_SIDE:     ("UP_SIDE",     self.__top_thickness),
            EnumSides.RIGHT_SIDE:  ("RIGHT_SIDE",  self.__right_thickness),
            EnumSides.BOTTOM_SIDE: ("BOTTOM_SIDE", self.__bottom_thickness),
            EnumSides.LEFT_SIDE:   ("LEFT_SIDE",   self.__left_thickness)
        }        
        if par_side_filter == EnumSides.ALL_SIDES:
            return {name: thickness for side, (name, thickness) in my_sides_map.items()}
        else:
            result = {}
            for side, (name, thickness) in my_sides_map.items():
                if par_side_filter & side:
                    result[name] = thickness
            return result
    @thickness.setter
    def thickness(self, par_thickness_dict:dict[EnumSides, int]):
        for side, thickness in par_thickness_dict.items():
            if side & EnumSides.UP_SIDE:
                self.__top_thickness = thickness
            if side & EnumSides.RIGHT_SIDE:
                self.__right_thickness = thickness
            if side & EnumSides.BOTTOM_SIDE:
                self.__bottom_thickness = thickness
            if side & EnumSides.LEFT_SIDE:
                self.__left_thickness = thickness
            else:
                raise ValueError(f"Invalid side name: {side}")
        return self
    
    @property
    def radius(self, par_corner_filter:EnumCorners=EnumCorners.ALL_CORNERS):
        my_corners_map = {
            EnumCorners.TOP_LEFT:     ("TOP_LEFT",     self.__top_left_radius),
            EnumCorners.TOP_RIGHT:    ("TOP_RIGHT",    self.__top_right_radius),
            EnumCorners.BOTTOM_RIGHT: ("BOTTOM_RIGHT", self.__bottom_right_radius),
            EnumCorners.BOTTOM_LEFT:  ("BOTTOM_LEFT",  self.__bottom_left_radius)
        }        
        if par_corner_filter == EnumSides.ALL_SIDES:
            return {name: radius for corner, (name, radius) in my_corners_map.items()}
        else:
            result = {}
            for corner, (name, radius) in my_corners_map.items():
                if par_corner_filter & corner:
                    result[name] = radius
            return result
    @radius.setter
    def radius(self, par_corner_dict:dict[EnumCorners, int]):
        for corner, radius in par_corner_dict.items():
            if corner & EnumCorners.TOP_LEFT:
                self.__top_left_radius = radius
            if corner & EnumCorners.TOP_RIGHT:
                self.__top_right_radius = radius
            if corner & EnumCorners.BOTTOM_RIGHT:
                self.__bottom_right_radius = radius
            if corner & EnumCorners.BOTTOM_LEFT:
                self.__bottom_left_radius= radius
            else:
                raise ValueError(f"Invalid corner name: {corner}")
        return self

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, value):
        self.__color = value
        return self
    

