from .Thigh.lib_LeftThigh import LeftThigh

class LeftLeg:
    
    thigh:LeftThigh = None

    def __init__(self):
        
        self.thigh = LeftThigh()
        print("Luna's left thigh has been initialized.")