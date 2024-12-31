from .ForeArm.lib_RightForeArm import RightForeArm

class RightArm:
    
    foreArm:RightForeArm = None

    def __init__(self):
        
        self.foreArm = RightForeArm()
        print("Luna's right arm has been initialized.")
        