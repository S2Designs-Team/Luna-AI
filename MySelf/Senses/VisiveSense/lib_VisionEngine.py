from AssetsLibs.Abstraction.lib_NeuralProcess import ANeuralProcess

class VisionEngine(ANeuralProcess):

    #- [CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__()

    def initialize(self):
        """
        Initializes the Vision Engine.
        """
        self.logger.info("[VisionEngine]::[Initialize]")        
        self.is_process_initialized = True

    async def handleSelfStimuli(self, message):
        """
        Elaborates the image stimuli simulating the vision sense.
        """
        self.logger.info("VisionEngine: processing vision image stimuli - %s", message)

        # Simulates the vision result
        result = f"Detected objects in image: {message}"
        self.logger.info("VisionEngine result: %s", result)
        return result
    
    async def handleExternalStimuli(self, message:str = ""):
        """
        Elaborates the image stimuli simulating the vision sense.
        """
        self.logger.info("VisionEngine: processing vision image stimuli - %s", message)

        # Simulates the vision result
        result = f"Detected objects in image: {message}"
        self.logger.info("VisionEngine result: %s", result)
        return result