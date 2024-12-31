from .Shin.lib_LeftShin import LeftShin

class LeftThigh:
    
    shin:LeftShin = None

    def __init__(self):
        
        self.shin = LeftShin()
        print("Luna's left shin has been initialized.")