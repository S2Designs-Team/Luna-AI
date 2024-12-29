from AssetsLibs.Abstraction.lib_NeuralProcess           import ANeuralProcess
from AssetsLibs.Helpers.Configuration.lib_Configuration import ConfigurationHelper
from MySelf.Senses.HearingSense.lib_HearingEngine       import HearingEngine
from MySelf.Senses.VisiveSense.lib_VisionEngine         import VisionEngine
from MySelf.Senses.TouchSense.lib_TouchEngine           import TouchEngine
from MySelf.Senses.SpeechSense.lib_SpeechEngine         import SpeechEngine
from MySelf.Senses.OlfactorySense.lib_OlfactoryEngine   import OlfactoryEngine
import logging                       # Utilizzato per il logging avanzato
import asyncio
import inspect
import os

class MySelf():

    _MY_SENSES:dict[str,ANeuralProcess] = {}
    _logger:logging.Logger              = None 
    _is_myself_initialized              = False
    _am_i_awake                         = False

    #- [CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------------
    def __init__(self, logger_manager=None):
        """
        Costruttore della classe MySelf.
        :param logger_manager: Oggetto di gestione del logging (LoggerManager).
        """
        # - Logger configuration
        # ----------------------------
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')
        #[sni] self.logger = logging.getLogger(__name__)
        if logger_manager is None:
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.INFO)
        else:
            self.logger = logger_manager

        # - Recupera il percorso completo del file del chiamante
        # ------------------------------------------------------
        caller_frame                        = inspect.stack()[1]
        caller_module                       = inspect.getmodule(caller_frame[0])
        if caller_module and hasattr(caller_module, "__file__"):
            self._script_path = os.path.abspath(__file__)
        else:
            raise RuntimeError("Impossibile determinare il percorso del file della classe concreta.")
        self._script_directory              = os.path.dirname(self._script_path)
        self._script_name                   = os.path.basename(self._script_path)
        
        # Configurazione
        self._config_name                   = "config.yaml"
        self._config_directory              = self._script_directory
        self._config_path                   = os.path.join(self._config_directory, self._config_name)
        self.configuration:dict             = self._loadConfiguration()            

    async def async_init(self):
        # Inizializzazione asincrona
        await self.initialize()

    async def initialize(self, senseName='MySelf'):
        """
        Inizializza i sensi e li aggiunge al dizionario `_MY_SENSES`.
        Ogni classe dei sensi deve completare la propria logica di inizializzazione prima di essere aggiunta.
        """
        self.logger.info("[MySelf]::[initialize]")

        self._MY_SENSES = {}
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
                self.logger.info("    ├──>'%s' sense initialization started...", sense_name)
                sense_instance:ANeuralProcess = sense_class()  # Istanzia la classe del senso
                self._MY_SENSES[sense_name] = sense_instance

                # Verifica se l'istanza ha 'is_process_initialized'
                if not hasattr(sense_instance, 'is_process_initialized'):
                    raise AttributeError(f"Sense '{sense_name}' lacks the 'is_process_initialized' attribute.")

                while not sense_instance.is_process_initialized:
                    await asyncio.sleep(3)

                self.logger.info("    ├──>'%s' sense has been succesfully initialized.", sense_name)
            except Exception as e:
                self.logger.error("[MySelf] => Error during the initialization of '%s': %s", sense_name, str(e))
                raise RuntimeError(f"['{sense_name}' SENSE] Initialization failure.") from e

        self._is_myself_initialized = True
        
    def _loadConfiguration(self):
        """ 
        Carica il file di configurazione 'config.yaml' presente nello stesso percorso della classe concreta.
        :return: Dizionario con la configurazione caricata. 
        """
        return ConfigurationHelper().loadConfiguration(self._config_directory)

    async def wakeUp(self):
        """
        """
        #- Simula il risveglio dei sensi
        #-------------------------------
        _ = await self._MY_SENSES["Hearing"].wakeUp()
        #_ = await self._MY_SENSES["Visual"].wakeUp()
        #_ = await self._MY_SENSES["Touch"].wakeUp()
        #_ = await self._MY_SENSES["Vocal"].wakeUp()
        #_ = await self._MY_SENSES["Olfactory"].wakeUp()
        self._am_i_awake = True
        return

    async def sleep(self):
        """
        """
        #self._MY_SENSES["Hearing"].sleep()
        #self._MY_SENSES["Visual"].sleep()
        #self._MY_SENSES["Touch"].sleep()
        #self._MY_SENSES["Vocal"].sleep()
        #self._MY_SENSES["Olfactory"].sleep()    
        self._am_i_awake = False   
        return
    
    async def turnOn(self):
        """
        """
        #if self.am_i_active:
        #    print("LUNA is already on... she is just waiting you to wake her up.")
        return

    async def turnOff(self):
        """
        """
        #if not self.am_i_active:
        #    print("LUNA is already off... just wait until each process finishes to turn off.")
        #    return
        #else: 
        _ = await self.sleep()
        
        self.am_i_active = False
        return
        
    async def handleSelfStimuli(self, message):
        """
        Elaborates internal (self) stimuli.
        """
        self.logger.info("Processing internal stimuli: %s", message)

        # Simulates the result of the processed internal (self) stimuli      
        result = f"Internal (self) stimuli: {message}"
        print(f"Processed internal (self) stimuli: result => {result}")
        return result

    async def handleExternalStimuli(self, message):
        """
        Elaborates external stimuli to simulate.
        """
        self.logger.info("Processing external stimuli: %s", message)

        # Simulates the result of the processed external stimuli        
        result = f"External stimuli: {message}"
        print(f"Processed external stimuli: result => {result}")
        return result