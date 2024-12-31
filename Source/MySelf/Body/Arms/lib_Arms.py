from .Left.lib_LeftArm   import LeftArm
from .Right.lib_RightArm import RightArm

class Arms:
    
    leftArm:LeftArm   = None
    rightArm:RightArm = None

    def __init__(self):

        self.leftArm = LeftArm()
        print("Luna's left arm has been initialized.")

        self.rightArm = RightArm()
        print("Luna's right arm has been initialized.")
