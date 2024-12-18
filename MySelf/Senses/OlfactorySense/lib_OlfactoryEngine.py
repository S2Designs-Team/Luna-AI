from AssetsLibs.Abstraction.lib_NeuralProcess import ANeuralProcess

class OlfactoryEngine(ANeuralProcess):

    #- [CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__()

    async def initialize(self):
        """
        Inizializza il motore di Text-to-Speech.
        """
        print("SpeechEngine => TextToSpeechEngine: initialized.")
    
    async def handleSelfStimuli(self, message):
        """
        Elaborates the Olfactory stimuli to simulate the Olfactory Sense.
        """
        print(f"OlfactoryEngine: processing olfactory stimuli - {message}")

        # Simulates the vocal speech result
        result = f"Synthesized smell: {message}"
        print(f"OlfactoryEngine result: {result}")
        return result

    async def handleExternalStimuli(self, message:str = ""):
        """
        Elaborates the Olfactory stimuli to simulate the Olfactory Sense.
        """
        print(f"OlfactoryEngine: processing olfactory stimuli - {message}")

        # Simulates the vocal speech result
        result = f"Synthesized smell: {message}"
        print(f"OlfactoryEngine result: {result}")
        return result