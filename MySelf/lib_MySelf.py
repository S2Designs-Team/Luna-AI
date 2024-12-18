from AssetsLibs.Abstraction.lib_NeuralProcess         import ANeuralProcess
from MySelf.Senses.HearingSense.lib_HearingEngine     import HearingEngine
from MySelf.Senses.VisiveSense.lib_VisionEngine       import VisionEngine
from MySelf.Senses.TouchSense.lib_TouchEngine         import TouchEngine
from MySelf.Senses.SpeechSense.lib_SpeechEngine       import SpeechEngine
from MySelf.Senses.OlfactorySense.lib_OlfactoryEngine import OlfactoryEngine

class MySelf(ANeuralProcess):

    _MY_SENSES:list[str, ANeuralProcess]  = None 

    #- [CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------------
    def __init__(self):
        self._MY_SENSES = {}
        super().__init__()

    async def initialize(self, senseName='MySelf'):
        """
        Inizializza i sensi e li aggiunge al dizionario `_MY_SENSES`.
        Ogni classe dei sensi deve completare la propria logica di inizializzazione prima di essere aggiunta.
        """
        senses_to_initialize = [
            ("Hearing",   HearingEngine),
            ("Visual",    VisionEngine),
            ("Touch",     TouchEngine),
            ("Vocal",     SpeechEngine),
            ("Olfactory", OlfactoryEngine),
            # Aggiungi altre classi di sensi qui se necessario
        ]

        for sense_name, sense_class in senses_to_initialize:
            try:
                self.logger.info("[MySelf] => Inizializzazione del senso '%s' in corso...", sense_name)
                sense_instance:ANeuralProcess = sense_class()  # Istanzia la classe del senso
                _ = await sense_instance.initialize()
                self._MY_SENSES[sense_name]   = sense_instance
                self.logger.info("[MySelf] => The '%s' sense has been succesfully initialized.", sense_name)
            except Exception as e:
                self.logger.error("[MySelf] => Error during the initialization of '%s': %s", sense_name, str(e))
                raise RuntimeError(f"['{sense_name}' SENSE] Initialization failure.") from e

    async def wakeUp(self):
        """
        """
        #- Simula il risveglio dei sensi
        #-------------------------------
        #_ = await self._MY_SENSES["Hearing"].wakeUp()
        #_ = await self._MY_SENSES["Visual"].wakeUp()
        #_ = await self._MY_SENSES["Touch"].wakeUp()
        #_ = await self._MY_SENSES["Vocal"].wakeUp()
        #_ = await self._MY_SENSES["Olfactory"].wakeUp()
        return

    async def sleep(self):
        """
        """
        #self._MY_SENSES["Hearing"].sleep()
        #self._MY_SENSES["Visual"].sleep()
        #self._MY_SENSES["Touch"].sleep()
        #self._MY_SENSES["Vocal"].sleep()
        #self._MY_SENSES["Olfactory"].sleep()       
        return
    
    async def turnOn(self):
        """
        """
        if self.am_i_active:
            print("LUNA is already on... she is just waiting you to wake her up.")
        return

    async def turnOff(self):
        """
        """
        if not self.am_i_active:
            print("LUNA is already off... just wait until each process finishes to turn off.")
            return
        else: 
            _ = await self.sleep()
        
        self.am_i_active = False
        return
        
    
    async def handleSelfStimuli(self, message):
        """
        Elaborates internal (self) stimuli.
        """
        # Simulates the result of the processed internal (self) stimuli 
        result = f"Internal (self) stimuli: {message}"
        print(f"Processed internal (self) stimuli: result => {result}")
        return result

    async def handleExternalStimuli(self, message):
        """
        Elaborates external stimuli to simulate.
        """
        # Simulates the result of the processed external stimuli 
        result = f"External stimuli: {message}"
        print(f"Processed external stimuli: result => {result}")
        return result