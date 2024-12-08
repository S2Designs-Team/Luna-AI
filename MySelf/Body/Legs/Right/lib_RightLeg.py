from .Thigh.lib_RightThigh import RightThigh

class RightLeg:
    
    thigh:RightThigh = None

    def __init__(self):
        
        self.thigh = RightThigh()
        print("Luna's right thigh has been initialized.")