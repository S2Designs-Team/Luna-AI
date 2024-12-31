from AssetsLibs.Abstraction.lib_NeuralProcess import ANeuralProcess

class TouchEngine(ANeuralProcess):

    #- [CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__()

    def initialize(self):
        """
        Initializes the Touch Engine.
        """
        self.logger.info("[TouchEngine]::[Initialize]")   
        self.is_process_initialized = True

    async def handleSelfStimuli(self, message):
        """
        Elaborates the touch stimuli to simulate the Touch Sense.
        """
        print(f"TouchEngine: processing the touch stimuli - {message}")

        # Simulates the touch result
        result = f"Detected Touch stimuli: {message}"
        print(f"TouchEngine result: {result}")
        return result
    
    async def handleExternalStimuli(self, message:str = ""):
        """
        Elaborates the touch stimuli to simulate the Touch Sense.
        """
        print(f"TouchEngine: processing the touch stimuli - {message}")

        # Simulates the touch result
        result = f"Detected Touch stimuli: {message}"
        print(f"TouchEngine result: {result}")
        return result