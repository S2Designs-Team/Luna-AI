from .Foot.lib_RightFoot import RightFoot

class RightShin:
    
    foot:RightFoot = None

    def __init__(self):
        
        self.foot = RightFoot()
        print("Luna's right foot has been initialized.")