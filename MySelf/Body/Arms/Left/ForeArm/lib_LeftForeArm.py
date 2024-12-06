from .Hand.lib_LeftHand import LeftHand

class LeftForeArm:

    hand = None

    def __init__(self):

        self.hand = LeftHand()
        print("Luna's left hand has been initialized.")
        