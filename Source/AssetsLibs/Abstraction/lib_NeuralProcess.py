# Copyright 2022 S2DesignsTeam (㊙️anonimo㊙️).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
import inspect
import os
import json
from pathlib import Path
import logging                       # Utilizzato per il logging avanzato
from abc import ABC, abstractmethod
from ..Helpers.Configuration.lib_Configuration import ConfigurationHelper

class ANeuralProcess(ABC):
    """
    Classe astratta per definire la struttura base di un processo neurale. 
    """
    _name:str                       = "ANeuralProcessBase"  # Nome di base del Processo Neurale
    _logger:logging.Logger          = None 
    _project_root:str               = None                  # Directory root del progetto (Directory)
    _script_directory:str           = None                  # Directory del file script (Directory)
    _script_name:str                = None                  # FileName dello script (FileName)
    _script_path:str                = None                  # Percorso del file script (Directory + FileName)
    
    _config_directory:str           = None                  # Directory del file di configurazione (Directory)
    _config_name:str                = None                  # FileName di configurazione (FileName)
    _config_path:str                = None                  # Percorso del file di configurazione (Directory + FileName)

    _configuration                  = None                  # Configurazione del processo letta dal file config.yaml

    _am_i_active:bool               = False                 # Flag che indica se il processo Neurale è attivo (True) o dormiente (False)
    __is_process_initialized:bool    = False
    _stimuli_queue                  = None                  # Variabile per la coda degli stimoli
    _external_stimuli_directory:str = None                  # Directory principale degli stimoli esterni

    #- [PROPERTIES]
    #--------------------------------------------------------------------------------------------------
    @property
    def am_i_active(self):
        """
        Verifica se il processo neurale è attivo.
        """
        return self._am_i_active
    
    @property
    def is_process_initialized(self):
        return self.__is_process_initialized

    @is_process_initialized.setter
    def is_process_initialized(self, value:bool):
        self.__is_process_initialized = value

    @property
    def script_directory(self): 
        """
        Directory dello script (Getter di proprietà).
        """
        return self._script_directory
    
    @script_directory.setter
    def script_directory(self, value):
        """
        Directory dello script (Setter di proprietà).
        """

        if isinstance(value, Path):  # Controllo opzionale per assicurarsi che sia un oggetto Path
            self._script_directory = value
        else:
            raise TypeError("script_directory deve essere un oggetto Path.")

    @property
    def script_name(self): 
        """
        Nome dello script (Getter di proprietà).
        """
        return self._script_name
   
    @script_name.setter
    def script_name(self, value):
        """
        Nome dello script (Setter di proprietà).
        """
        self._script_name = value

    @property
    def script_path(self): 
        """
        Percorso dello script (Getter di proprietà).
        """
        return self._script_path
   
    @script_path.setter
    def script_path(self, value):
        """
        Percorso dello script (Setter di proprietà).
        """
        if isinstance(value, Path):  # Controllo opzionale per assicurarsi che sia un oggetto Path
            self._script_path = value
        else:
            raise TypeError("script_path deve essere un oggetto Path.")
            

    @property
    def config_directory(self): 
        """
        Directory del file di configurazione (Getter di proprietà).
        """
        return self._config_directory
    
    @script_directory.setter
    def script_directory(self, value):
        """
        Directory del file di configurazione (Setter di proprietà).
        """

        if isinstance(value, Path):  # Controllo opzionale per assicurarsi che sia un oggetto Path
            self._config_directory = value
        else:
            raise TypeError("config_directory deve essere un oggetto Path.")
        
    @property
    def config_name(self): 
        """
        Nome del file di configurazione (Getter di proprietà).
        """
        return self._config_name
   
    @config_name.setter
    def config_name(self, value):
        """
        Nome del file di configurazione (Setter di proprietà).
        """
        if isinstance(value, str):  # Controllo opzionale per assicurarsi che sia un oggetto str
            self.config_name = value
        else:
            raise TypeError("config_name deve essere un oggetto str.")

    @property
    def config_path(self): 
        """
        Percorso del file di configurazione (Getter di proprietà).
        """
        return self._config_path
   
    @config_path.setter
    def config_path(self, value):
        """
        Percorso del file di configurazione (Setter di proprietà).
        """
        if isinstance(value, str):  # Controllo opzionale per assicurarsi che sia un oggetto Path
            self._config_path = value
        else:
            raise TypeError("config_path deve essere un oggetto Path.")

    @property
    def external_stimuli_directory(self):
        """
        """
        return self._external_stimuli_directory
    
    @external_stimuli_directory.setter
    def external_stimuli_directory(self, value):
        """
        """
        self._external_stimuli_directory = value


    #- [CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Initializes the Neural Process by automatically loading the config.yaml 
        file from the script's path.
        """
        # - Logger configuration
        # ----------------------------
        #logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
        self.logger = logging.getLogger(__name__)

        # - Retrieves the full path of the application's entry point
        # ----------------------------------------------------------
        app_entry_frame                     = inspect.stack()[-1]
        main_module                         = app_entry_frame.filename
        self._project_root                  = os.path.dirname(main_module)

        # - Retrieves the full file path of the caller
        # --------------------------------------------
        caller_frame                        = inspect.stack()[1]
        caller_module                       = inspect.getmodule(caller_frame[0])
        if caller_module and hasattr(caller_module, "__file__"):
            self._script_path = os.path.abspath(caller_module.__file__)
        else:
            raise RuntimeError("Unable to determine the file path of the concrete class.")
        self._script_directory              = os.path.dirname(self._script_path)
        self._script_name                   = os.path.basename(self._script_path)
        
        self._config_name                   = "config.yaml"
        self._config_directory              = self._script_directory
        self._config_path                   = os.path.join(self.config_directory, self.config_name)

        self.configuration:dict             = self._loadConfiguration()
        self._external_stimuli_directory    = os.path.join(self._project_root, "MySelf\\Senses\\_ExternalStimuli\\")

        self._initializationTask            = None
        self._incomingStimuliEvaluationTask = None

        self.initialize()
        self._stimuli_queue                 = asyncio.Queue()  # Coda per la comunicazione tra processi neurali

        
    def _loadConfiguration(self):
        """ 
        Loads the 'config.yaml' configuration file located in the same path as the concrete class.
        :return: Dictionary with the loaded configuration. 
        """
        return ConfigurationHelper().loadConfiguration(self.config_directory)
    
    async def _readExternalStimuli(self):
        """
        Reads the JSON files from the input directory and returns a list of stimuli.
        :return: List of dictionaries representing the stimuli.
        """
        if not self.external_stimuli_directory:
            raise ValueError(f"[{self.__class__.__name__}] Input directory for external stimuli not configured.")
        
        stimuli = []
        for filename in os.listdir(self._esternalStimuliDir):
            file_path = os.path.join(self._esternalStimuliDir, filename)
            if filename.endswith('.json'):
                try:
                    with open(file_path, 'r') as f:
                        stimuli.append(json.load(f))
                except json.JSONDecodeError as e:
                    self.logger.error("[%s] Error while decoding %s: %s", self.__class__.__name__, filename, e)

                except Exception as e:
                    print(f"[{self.__class__.__name__}] Error while reading {filename}: {e}")
                finally:
                    try:
                        if os.Path.exists(file_path):
                            os.remove(file_path)  # Deletes the file after reading
                            self.logger.info("[%s] External stimulus file removed %s: %s", self.__class__.__name__, file_path, e)
                    except Exception as e:
                        self.logger.warning("[%s] Unable to delete the external stimulus file %s: %s", self.__class__.__name__, file_path, e)
        return stimuli

    async def _evaluateIncomingStimuli(self):
        """
        Manages asynchronous communication (e.g., receiving messages).
        """
        while self.am_i_active:
            try:            
                #neuralStimuli = await self._stimuli_queue.get()
                #externalStimuli = await self._readExternalStimuli()
                #if neuralStimuli:
                #    await self.handleSelfStimuli(neuralStimuli)
                #if externalStimuli:
                await self.handleExternalStimuli()        

            except asyncio.CancelledError:
                self.logger.info("[%s] Stimuli evaluation interrupted.", self.__class__.__name__)
                break

            except Exception as e:
                self.logger.error("[%s] Error during stimuli evaluation: %s", self.__class__.__name__, str(e))

    async def initializeTask(self):
        """
        Metodo astratto implementato dalla classe concreta
        """
        self._initializationTask            = asyncio.create_task(self.initialize())
        while not self.is_process_initialized:
            try:
                _ = await asyncio.sleep(0.1)
            except asyncio.CancelledError:
                self.logger.info("[%s] Initialization interruption.", self.__class__.__name__)
                break

            except Exception as e:
                self.logger.error("[%s] Error occurred during the initialization: %s", self.__class__.__name__, str(e))

    @abstractmethod
    def initialize(self):
        """
        [Abstract Method - It must be implemented by concrete classes.]/\n
        Initializes the Neural Process.
        This method is used to assign configuration values specific to the Neural 
        Process being executed and to instantiate components required for its operation.
        """
        pass

    @abstractmethod
    async def handleSelfStimuli(self, message):
        """
        [Abstract Method - It must be implemented by concrete classes.]\n
        Handles the Neural Stimulus present in the Message Queue of internal stimuli.
        At the moment this method is called, the Neural Process still does not know 
        if the stimulus is something it needs to consider and process.
        Inside this method, the check logic must be defined, enabling the Neural 
        Process to determine whether the stimulus should be considered and its own 
        reprocessing logic.
        If necessary, the sendStimuli method can be called from here, which sends a 
        new stimulus with the result of the Neural Process's reprocessing of the 
        previous stimulus.
        :param message: Internal stimulus message.
        """
        pass

    @abstractmethod
    async def handleExternalStimuli(self, message):
        """
        [Abstract method - It must be implemented by concrete classes.]\n
        Handles the Neural Stimulus present in the Message Queue of external stimuli.
        At the moment this method is called, the Neural Process still does not know 
        if the stimulus is something it needs to consider and process.
        Inside this method, the check logic must be defined, enabling the Neural 
        Process to determine whether the stimulus should be considered and its own 
        reprocessing logic.
        Here, the sendStimuli method must be called to send the external stimulus to 
        the message queue so that it can be processed by the appropriate Neural Process.
        : param message: External stimulus message.
        """
        pass

    async def sendStimuli(self, stimuli):
        """
        Method for communication between the various neural processes.
        :param stimuli: Dictionary with processed data.
        """
        try:
            await self._stimuli_queue.put(stimuli)
            self.logger.info("[%s] Stimuli sent: %s", self.__class__.__name__, stimuli)
        except Exception as e:
            self.logger.error("[%s] Error during stimuli sending: %s", self.__class__.__name__, e)

    async def wakeUp(self):
        """
        Activates the Neural Process and starts the thread for its logic
        (definded in the concrete class within the handleStimuli method)
        """
        self.logger.info("[%s] Starting the Neural Process...", self.__class__.__name__)

        if self._am_i_active:
            raise RuntimeError("The Neural Process is already active.")
         

        self._am_i_active = True

        # Avvia il task asincrono per gestire gli stimoli
        self._incomingStimuliEvaluationTask = asyncio.create_task(self._evaluateIncomingStimuli())

    async def sleep(self):
        """
        Sets the Neural Process to rest (stops the stimulus processing logic).
        """
        if not self.am_i_active:
            raise RuntimeError("Neural process is not active.")        
        
        self._am_i_active = False
        if self._incomingStimuliEvaluationTask:
            # Annulla il task
            self._incomingStimuliEvaluationTask.cancel()
        try:
            await self._incomingStimuliEvaluationTask
        except asyncio.CancelledError:
            self.logger.info("[%s] Process is now in sleep mode.", self.__class__.__name__)
        except Exception as e:
            self.logger.error("[%s] Error occurred during the process sleep mode: %s", self.__class__.__name__, e)
        finally:
            self._incomingStimuliEvaluationTask = None