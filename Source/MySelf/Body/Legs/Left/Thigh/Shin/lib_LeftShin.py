from .Foot.lib_LeftFoot import LeftFoot

class LeftShin:
    
    foot:LeftFoot = None

    def __init__(self):
        
        self.foot = LeftFoot()
        print("Luna's left foot has been initialized.")