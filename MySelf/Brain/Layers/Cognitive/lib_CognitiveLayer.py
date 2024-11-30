from AssetsLibs.Abstraction.lib_NeuralProcess     import ANeuralProcess
from MySelf.Senses.VisiveSense.lib_VisionEngine   import VisionEngine
from MySelf.Senses.HearingSense.lib_HearingEngine import HearingEngine
from MySelf.Senses.SpeechSense.lib_SpeechEngine   import SpeechEngine

# Classe derivata che simula il layer del processo Cognitivo del cervello
class CognitiveLayer(ANeuralProcess):
    def __init__(self):
        super().__init__()
        self.vision_engine = VisionEngine()
        self.stt_engine    = HearingEngine("")
        self.tts_engine    = SpeechEngine()

    async def initialize(self):
        """
        Inizializza tutti i motori del layer cognitivo.
        """
        await self.vision_engine.wakeUp()
        await self.stt_engine.wakeUp()
        await self.tts_engine.wakeUp()
        print("CognitiveLayer: all engines initialized.")

    async def handleSelfStimuli(self, message):
        """Distribuisce il messaggio al motore appropriato."""
        if message["type"] == "image":
            return await self.vision_engine.send_stimulus(message["data"])
        elif message["type"] == "audio":
            return await self.stt_engine.send_stimulus(message["data"])
        elif message["type"] == "text":
            return await self.tts_engine.send_stimulus(message["data"])
        else:
            print(f"CognitiveLayer: Unknown stimulus type {message}")
        return
    
    async def handleExtrernalStimuli(self, message):
        """Distribuisce il messaggio al motore appropriato."""
        if message["type"] == "image":
            return await self.vision_engine.send_stimulus(message["data"])
        elif message["type"] == "audio":
            return await self.stt_engine.send_stimulus(message["data"])
        elif message["type"] == "text":
            return await self.tts_engine.send_stimulus(message["data"])
        else:
            print(f"CognitiveLayer: Unknown stimulus type {message}")
        return


    async def sleep(self):
        """Mette a riposo tutti i motori."""
        await self.vision_engine.sleep()
        await self.stt_engine.sleep()
        await self.tts_engine.sleep()
        print("CognitiveLayer: all engines stopped.")