from .Left.lib_LeftLeg   import LeftLeg
from .Right.lib_RightLeg import RightLeg

class Legs:
    
    leftLeg:LeftLeg   = None
    rightLeg:RightLeg = None

    def __init__(self):

        self.leftLeg = LeftLeg()
        print("Luna's left leg has been initialized.")

        self.rightLeg = RightLeg()
        print("Luna's right leg has been initialized.")
