from .Shin.lib_RightShin import RightShin

class RightThigh:
    
    shin:RightShin = None

    def __init__(self):
        
        self.shin = RightShin()
        print("Luna's right shin has been initialized.")