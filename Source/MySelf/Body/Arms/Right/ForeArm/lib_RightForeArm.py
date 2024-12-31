from .Hand.lib_RightHand import RightHand

class RightForeArm:

    hand = None

    def __init__(self):

        self.hand = RightHand()
        print("Luna's right fore arm has been initialized.")
        