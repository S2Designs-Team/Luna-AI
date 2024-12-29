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
        Inizializza il Processo Neurale caricando automaticamente il file config.yaml 
        dal percorso dello script.
        """
        # - Logger configuration
        # ----------------------------
        #logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
        self.logger = logging.getLogger(__name__)

        # - Recupera il percorso completo dell'entry point dell'applicazione
        # ------------------------------------------------------------------
        app_entry_frame                     = inspect.stack()[-1]
        main_module                         = app_entry_frame.filename
        self._project_root                  = os.path.dirname(main_module)

        # - Recupera il percorso completo del file del chiamante
        # ------------------------------------------------------
        caller_frame                        = inspect.stack()[1]
        caller_module                       = inspect.getmodule(caller_frame[0])
        if caller_module and hasattr(caller_module, "__file__"):
            self._script_path = os.path.abspath(caller_module.__file__)
        else:
            raise RuntimeError("Impossibile determinare il percorso del file della classe concreta.")
        self._script_directory              = os.path.dirname(self._script_path)
        self._script_name                   = os.path.basename(self._script_path)
        
        self._config_name                   = "config.yaml"
        self._config_directory              = self._script_directory
        self._config_path                   = os.path.join(self.config_directory, self.config_name)

        self.configuration:dict             = self._loadConfiguration()
        self._external_stimuli_directory    = os.path.join(self._project_root, "MySelf\\Senses\\_ExternalStimuli\\")

        self._ininitializationTask          = None
        self._incomingStimuliEvaluationTask = None
        # [sni] bla bla bla
        # self._ininitializationTask          = asyncio.create_task(self.initializeTask())
        self.initialize()
        self._stimuli_queue                 = asyncio.Queue()  # Coda per la comunicazione tra processi neurali

        
    def _loadConfiguration(self):
        """ 
        Carica il file di configurazione 'config.yaml' presente nello stesso percorso della classe concreta.
        :return: Dizionario con la configurazione caricata. 
        """
        return ConfigurationHelper().loadConfiguration(self.config_directory)
    
    async def _readExternalStimuli(self):
        """
        Legge i file JSON dalla directory di input e restituisce una lista di stimoli.
        :return: Lista di dizionari rappresentanti gli stimoli.
        """
        if not self.external_stimuli_directory:
            raise ValueError(f"[{self.__class__.__name__}] Directory di input per gli stimoli esterni non configurata.")
        
        stimuli = []
        for filename in os.listdir(self._esternalStimuliDir):
            file_path = os.path.join(self._esternalStimuliDir, filename)
            if filename.endswith('.json'):
                try:
                    with open(file_path, 'r') as f:
                        stimuli.append(json.load(f))
                except json.JSONDecodeError as e:
                    self.logger.error("[%s] Errore nella decodifica di %s: %s", self.__class__.__name__, filename, e)

                except Exception as e:
                    print(f"[{self.__class__.__name__}] Errore durante la lettura di {filename}: {e}")
                finally:
                    try:
                        if os.Path.exists(file_path):
                            os.remove(file_path)  # Elimina il file dopo la lettura
                            self.logger.info("[%s] File di stimolo esterno rimosso %s: %s", self.__class__.__name__, file_path, e)
                    except Exception as e:
                        self.logger.warning("[%s] Impossibile eliminare il file di stimolo esterno %s: %s", self.__class__.__name__, file_path, e)
        return stimuli

    async def _evaluateIncomingStimuli(self):
        """
        Gestisce la comunicazione asincrona (ad esempio ricevere messaggi).
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
                self.logger.info("[%s] Valutazione stimoli interrotta.", self.__class__.__name__)
                break

            except Exception as e:
                self.logger.error("[%s] Errore durante la valutazione degli stimoli: %s", self.__class__.__name__, str(e))

    async def initializeTask(self):
        # Metodo astratto implementato dalla classe concreta
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
        Metodo astratto per l'inizializzazione del Processo Neurale.
        Deve essere implementato dalle classi concrete.
        Da utilizzare per attribuire i valori di configurazione propri al Processo Neurale 
        che viene eseguito e ad istanziare componenti impiegati per il proprio funzionamento.
        """
        pass

    @abstractmethod
    async def handleSelfStimuli(self, message):
        """
        Gestisce lo Stimolo Neurale presente nella Message Queue degli stimoli interiori. 
        Al momento del richiamo di questo metodo il Processo Neurale 
        ancora non sa se è uno stimolo che deve tenere in considerazione ed elaborare.
        Qui dentro deve essere definita la logica check che serve al Processo Neurale per 
        capire se lo stimolo deve essere considerato e la propria logica di rielaborazione.
        Se è necessario da qui si può chiamare il metodo sendStimuli che invia un nuovo 
        stimolo con il risultato della rielaborazione del Processo Neurale effettuata sul 
        precedente stimolo.
        """
        pass

    @abstractmethod
    async def handleExternalStimuli(self, message):
        """
        Gestisce lo Stimolo Neurale presente nella Message Queue degli stimoli esterni. 
        Al momento del richiamo di questo metodo il Processo Neurale 
        ancora non sa se è uno stimolo che deve tenere in considerazione ed elaborare.
        Qui dentro deve essere definita la logica check che serve al Processo Neurale per 
        capire se lo stimolo deve essere considerato e la propria logica di rielaborazione.
        Qui si deve richiamare il metodo sendStimuli che invia lo stimolo esterno al message queue
        con per poter essere processato dal Processo Neurale di competenza.
        """
        pass

    async def sendStimuli(self, stimuli):
        """
        Metodo per la comunicazione tra i vari processi neurali.
        :param stimuli: Dizionario con i dati elaborati.
        """
        try:
            await self._stimuli_queue.put(stimuli)
            self.logger.info("[%s] Stimolo inviato: %s", self.__class__.__name__, stimuli)
        except Exception as e:
            self.logger.error("[%s] Errore durante l'invio dello stimolo: %s", self.__class__.__name__, e)

    async def wakeUp(self):
        """
        Attiva il Processo Neurale e fa partire il thread della propria logica
        (definita nella classe concreta all'interno del metodo handleStimuli).
        """
        self.logger.info("[%s] Avvio del Processo Neurale...", self.__class__.__name__)

        if self._am_i_active:
            raise RuntimeError("Il Processo Neurale è già attivo.")
         

        self._am_i_active = True

        # Avvia il task asincrono per gestire gli stimoli
        self._incomingStimuliEvaluationTask = asyncio.create_task(self._evaluateIncomingStimuli())

    async def sleep(self):
        """
        Mette il Processo Neurale a riposo (ferma la logica di processamento degli stimoli).
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