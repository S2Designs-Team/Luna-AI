from AssetsLibs.Abstraction.lib_NeuralProcess import ANeuralProcess

class TouchEngine(ANeuralProcess):
    async def initialize(self, senseName):
        """
        Initializes the Touch Engine.
        """
        print("TouchEngine: initialized.")

    async def handleSelfStimuli(self, message):
        """
        Elaborates the touch stimuli to simulate the Touch Sense.
        """
        print(f"TouchEngine: processing the touch stimuli - {message}")

        # Simulates the touch result
        result = f"Detected Touch stimuli: {message}"
        print(f"TouchEngine result: {result}")
        return result
    
    async def handleExternalStimuli(self, message):
        """
        Elaborates the touch stimuli to simulate the Touch Sense.
        """
        print(f"TouchEngine: processing the touch stimuli - {message}")

        # Simulates the touch result
        result = f"Detected Touch stimuli: {message}"
        print(f"TouchEngine result: {result}")
        return result