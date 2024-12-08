from .Arms.lib_Arms import Arms
from .Legs.lib_Legs import Legs

class Body:

    arms:Arms = None
    arms:Legs = None

    def __init__(self):

        self.arms = Arms()
        print("Luna's arms body parts have been initialized.")

        self.legs = Legs()
        print("Luna's legs body parts have been initialized.")