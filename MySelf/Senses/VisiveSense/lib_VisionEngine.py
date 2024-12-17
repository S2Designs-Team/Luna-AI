from AssetsLibs.Abstraction.lib_NeuralProcess import ANeuralProcess

class VisionEngine(ANeuralProcess):
    async def initialize(self, senseName):
        """
        Initializes the Vision Engine.
        """
        print("VisionEngine: initialized.")

    async def handleSelfStimuli(self, message):
        """
        Elaborates the image stimuli simulating the vision sense.
        """
        print(f"VisionEngine: processing vision image stimuli - {message}")

        # Simulates the vision result
        result = f"Detected objects in image: {message}"
        print(f"VisionEngine result: {result}")
        return result
    
    async def handleExtrernalStimuli(self):
        """
        Elaborates the image stimuli simulating the vision sense.
        """
        print(f"VisionEngine: processing vision image stimuli - {message}")

        # Simulates the vision result
        result = f"Detected objects in image: {message}"
        print(f"VisionEngine result: {result}")
        return result