from .ForeArm.lib_LeftForeArm import LeftForeArm

class LeftArm:

    foreArm:LeftForeArm = None

    def __init__(self):

        self.foreArm = LeftForeArm()
        print("Luna's left fore arm has been initialized.")
        
        