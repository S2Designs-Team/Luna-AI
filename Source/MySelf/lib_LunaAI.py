import asyncio
import time 
from AssetsLibs.Abstraction.lib_BasicProcess          import BasicProcess
from AssetsLibs.Abstraction.lib_NeuralProcess         import NeuralProcess
from MySelf.Senses.HearingSense.lib_HearingSense      import HearingSense
from MySelf.Senses.VisiveSense.lib_VisionSense        import VisionSense

class LunaAI(BasicProcess):
    _senses_instances:dict = None
    _am_i_sleeping:bool    = False

    @property
    def am_i_sleeping(self):
        for _ , sense_instance in self._senses_instances.items():
            processed_sense_instance:NeuralProcess = sense_instance
            self._am_i_sleeping = self._am_i_sleeping & (not processed_sense_instance.am_i_active)
        return self._am_i_sleeping
    
    def printProperties(self):
        self.LOGGER.debug("Project root:..................... %s", self.PROJECT_ROOT)
        self.LOGGER.debug("Concrete class name:.............. %s", self.CLASS_NAME)
        self.LOGGER.debug("Concrete class file name:......... %s", self.CLASS_FILE_NAME)
        self.LOGGER.debug("Concrete class path:.............. %s", self.CLASS_PATH)
        self.LOGGER.debug("Concrete class config file name:.. %s", self.CONFIG_FILENAME)
        self.LOGGER.debug("Concrete class config directory:.. %s", self.CONFIG_DIRECTORY)
        self.LOGGER.debug("Concrete class config path:....... %s", self.CONFIG_PATH)

    def initialize(self):
        """
        Performs the specific operations of the concrete process.
        """
        self.printProperties()
        self.LOGGER.info("[LunaAI]::[initialize]")

        self._senses_instances = {}
        senses_to_initialize = self.get_senses_to_initialize()
        
        for sense_name, sense_class in senses_to_initialize:
            try:
                self.LOGGER.info("    ├──> '%s' sense initialization started...", sense_name)
                sense_instance= sense_class()  # Istanzia la classe del senso
                sense_instance.start()
                self._senses_instances[sense_name] = sense_instance

                while not sense_instance.is_process_initialized:
                    time.sleep(0.1)

                self.LOGGER.info("    ├──>'%s' sense has been succesfully initialized.", sense_name)
            except Exception as e:
                self.LOGGER.error("[LunaAI]::[initialize] Error initializing '%s': %s", sense_name, str(e))
                raise RuntimeError(f"Initialization failed for sense '{sense_name}': {e}")

        self._is_myself_initialized = True
    
    async def elaboration(self):
        """
        Specific processing logic for the process.
        """
        self.LOGGER.info("[LunaAI]::[elaboration][+] Starting main processing loop.")

        if not self._senses_instances:
            self.LOGGER.warning("[LunaAI]::[elaboration] No senses initialized.")
            return

        try:
            while not self.am_i_sleeping:
                for sense_name, sense_instance in self._senses_instances.items():
                    processed_sense_instance:NeuralProcess = sense_instance
                    processed_sense_name:str               = sense_name
                    if processed_sense_instance.am_i_active:
                        self.LOGGER.debug("[LunaAI]::[elaboration] Sense '%s' is active.", processed_sense_name)
                    else:
                        self.LOGGER.debug("[LunaAI]::[elaboration] Sense '%s' is in sleep mode.", processed_sense_name)

                await asyncio.sleep(1)  # Idle sleep per il ciclo principale
        except Exception as e:
            self.LOGGER.error("[LunaAI]::[elaboration] Unexpected error: %s", str(e))
            raise RuntimeError("Elaboration failed.")
        self.LOGGER.info("[LunaAI]::[elaboration][-] Main loop ended.")

    async def wakeUp(self):
        for sense_name, sense_instance in self._senses_instances.items():
            processed_sense_instance:NeuralProcess = sense_instance
            processed_sense_name:str               = sense_name
            try:
                await processed_sense_instance.wakeUp()
            except Exception as e:
                self.LOGGER.error("[LunaAI] => Error during the awakening of sense '%s': %s", processed_sense_name, str(e))
                raise RuntimeError(f"['{processed_sense_name}' SENSE] wakingUp failure: {e}")
        
        self.LOGGER.info("[LunaAI]::[elaboration][-]")
        _ = await self._run()

    async def sleep(self):
        for sense_name, sense_instance in self._senses_instances.items():
            processed_sense_instance:NeuralProcess = sense_instance
            processed_sense_name:str               = sense_name
            try:
                await processed_sense_instance.sleep()
            except Exception as e:
                self.LOGGER.error("[LunaAI] => Error putting to sleep the '%s' sense : %s", processed_sense_name, str(e))
                raise RuntimeError(f"['{processed_sense_name}' SENSE] Putting to sleep failure: {e}")

        self.LOGGER.info("[LunaAI]::[elaboration][-]")
        _ = await self._run()        

    def get_senses_to_initialize(self):
        """
        Returns a Lists with all the itializable senses
        """
        my_senses_list = [
            ("Hearing", HearingSense),
            ("Vision", VisionSense)
        ]
        return my_senses_list
    