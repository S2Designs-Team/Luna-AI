import asyncio
import multiprocessing
import os
import inspect
import logging
from abc                                                       import ABC, abstractmethod
import sys
from AssetsLibs.Helpers.LogManager.lib_LogManager              import LoggerManager
from AssetsLibs.Helpers.Configuration.lib_Configuration        import ConfigurationHelper
from AssetsLibs.Helpers.MessageLogManagement.lib_ProcessLogger import ProcessLogger  # Aggiunto import per ProcessLogger

class BasicProcess(ABC):

    #- [PRIVATE OBJECTS]
    #--------------------------------------------------------------------------------------------------
    __logger:ProcessLogger             = None   # Logger specifico
    _process:multiprocessing.Process   = None   # Oggetto processo

    #- [PRIVATE FIELDS]
    #--------------------------------------------------------------------------------------------------
    _project_root:str                  = None   # Directory root del progetto (Directory)
    _concrete_class_name:str           = None   # Nome della classe concreta (ClassName)
    _script_directory:str              = None   # Directory del file script (Directory)
    _script_file_name:str              = None   # FileName dello script della classe concreta (FileName)
    _script_path:str                   = None   # Percorso del file script (Directory + FileName)
    
    __config_directory:str             = None   # Directory del file di configurazione (Directory)
    __config_file_name:str             = None   # FileName di configurazione (FileName)
    __config_path:str                  = None   # Percorso del file di configurazione (Directory + FileName)
    __configuration:dict               = None   # Configurazione della classe concreta (Dictionary)

    _is_process_initialized:bool       = False  # Flag di inizializzazione del processo
    
    @property
    def is_process_initialized(self):
        return self._is_process_initialized
    
    @is_process_initialized.setter
    def is_process_initialized(self, value:bool):
        self._is_process_initialized = value
    
    #- [PROPERTIES]
    #--------------------------------------------------------------------------------------------------
    @property
    def PROJECT_ROOT(self):
        """
        Readonly Property: The full path of the application's entry point.
        """   
        return self._project_root
    
    @property
    def CLASS_NAME(self):
        """
        Readonly Property: The name of the concrete class.
        """
        return self._concrete_class_name 

    @property
    def CLASS_DIRECTORY(self):
        """
        Readonly Property: The directory of the concrete class.
        """
        return self._script_directory

    @property
    def CLASS_PATH(self):
        """
        Readonly Property: The file path of the concrete class.
        """
        return self._script_path
    
    @property
    def CLASS_FILE_NAME(self):
        """
        Readonly Property: The file name of the concrete class.
        """
        return self._script_file_name

    @property
    def configuration(self):
        return self.__configuration

    @property
    def CONFIG_DIRECTORY(self):
        """
        Property: The configuration directory.\n\n
        If the configuration directory is not set,
        it is the script directory.
        """
        if not self.__config_directory:
            self.__config_directory = self._script_directory
        return self.__config_directory
    @CONFIG_DIRECTORY.setter
    def CONFIG_DIRECTORY(self, value):
        """
        Args:
            value (str): The path to the configuration directory.
        Raises:
            TypeError: If the provided value is not a string.
        """
        if isinstance(value, str):
            self.__config_directory = value
            self.__config_path = os.path.join(self.CONFIG_DIRECTORY, self.CONFIG_FILENAME)
        else:
            raise TypeError("CLASS_CONFIG_DIRECTORY must be string.")

    @property
    def CONFIG_FILENAME(self):
        """
        Property: The configuration File Name.
        """
        return self.__config_file_name
    @CONFIG_FILENAME.setter
    def CONFIG_FILENAME(self, value):
        """
        Args:
            value (str): The name of the configuration file.
        Raises:
            TypeError: If the provided value is not a string.
        """
        if isinstance(value, str):
            self.__config_file_name = value
            self.__config_path = os.path.join(self.CONFIG_DIRECTORY, self.CONFIG_FILENAME)
        else:
            raise TypeError("CLASS_CONFIG_FILENAME must be string.")   
       
    @property
    def CONFIG_PATH(self):
        """
        Readonly Property: The configuration File Path.
        """        
        return os.path.join(self.__config_path)

        """
        Configuration File Path (Property Setter).
        """
        if isinstance(value, str):
            self._config_path = value
        else:
            raise TypeError("CLASS_CONFIG_PATH must be string.")
    
    @property
    def LOGGER(self):
        """
        The logger instance associated with this object.
        """
        return self.__logger

    #- [CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Initializes the BasicProcess class by performing the following steps:\n\n
        1. Retrieves the execution root directory.
        2. Retrieves the concrete class name.
        3. Retrieves the absolute path of the concrete class.
        4. Retrieves the file name of the concrete class.
        5. Retrieves the directory of the concrete class.
        6. Retrieves the configuration file name.
        7. Initializes the logger.
        8. Loads the configuration.
        """
        self.__getExcecutionRoot()
        self.__getConcreteClassName()
        self.__getConcreteClassAbsPath()
        self.__getConcreteClassFileName()
        self.__getConcreteClassDirectory()
        self.__getConfigFileName()

        self.__initializeLogger()
        self.__loadConfiguration()

    #- [ABSTRACT METHODS]
    #--------------------------------------------------------------------------------------------------
    @abstractmethod
    def initialize(self):
        """
        [Abstract Method - It must be implemented by concrete classes.]/\n
        Initializes the Basic Process.
        This method is used to assign configuration values, specific to the 
        Process being executed, and to instantiate components required for 
        its operations.
        The Shadow call is done by constructor.
        """
        raise NotImplementedError("[%s] Must implement the 'initialize' method.", self.CLASS_NAME)
        pass
   
    @abstractmethod
    async def elaboration(self):
        """
        [Abstract Method - It must be implemented by concrete classes.]/\n
        Abstract Method to define the main elaboration logic for the concrete process.
        """
        raise NotImplementedError("[%s] Must implement the 'elaboration' method.", self.CLASS_NAME)
        pass
    
    #- [EXPOSED METHODS]
    #--------------------------------------------------------------------------------------------------
    def start(self):
        """
        This method starts the elaboration in a separate process.
        """
        logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - [%(levelname)s] - %(message)s")

        try:
            self.initialize()
        except Exception as e:
            raise RuntimeError(f"Error during the process execution: {e}")        
    
    def getConfigValue(self, *keys):
        """
        Retrieves the value from the configuration given a series of keys.\n\n
        Args:
            *keys: A variable length argument list of keys to traverse the configuration dictionary.
        Returns:
            The value from the configuration if all keys exist, otherwise None.
        Raises:
            KeyError: If any of the keys do not exist in the configuration.            
        Logs:
            Logs a warning message if any key does not exist in the configuration.
        """      
        try:
            config_value = self.configuration
            for key in keys:
                config_value = config_value[key]
            return config_value
        except KeyError:
            self.LOGGER.warning("ATTENTION: No configuration key %s has been setted in the config.yaml file.", ' -> '.join(keys), exc_info=True)
            return None

    def appendConfiguration(self, par_config_path:str = None):
        """
        Appends additional configuration to the existing configuration.

        This method loads a configuration from the specified path or from the default
        configuration path (self.CONFIG_PATH) and appends it to the current configuration.

        Args:
            par_config_path (str, optional): The path to the configuration file to be loaded.
                                                If not provided, the default configuration path
                                                (self.CONFIG_PATH) will be used.

        Returns:
            The updated configuration after appending the new configuration.
        """
        new_config = ConfigurationHelper().loadConfiguration(par_config_path)
        if isinstance(self._configuration, dict) and isinstance(new_config, dict):
            self._configuration.update(new_config) 
        else:
            raise TypeError("Configurations must be dictionaries to append.")
        return self._configuration
    
    #- [PRIVATE METHODS]
    #--------------------------------------------------------------------------------------------------
    def __getExcecutionRoot(self):
        """
        Returns the full path of the application's entry point.
        """
        try:
            # Se il modulo principale è __main__, ottieni il percorso
            if hasattr(sys, 'argv') and sys.argv:
                main_module = sys.argv[0]  # Ottieni il modulo principale dal comando di esecuzione

            # Calcola la directory del progetto
            self._project_root = os.path.dirname(os.path.abspath(main_module))

            # Verifica che la directory sia valida
            if not os.path.isdir(self._project_root):
                raise RuntimeError(f"Invalid project root directory: {self._project_root}")

        except Exception as e:
            raise RuntimeError(f"Error determining execution root: {e}")

        return self._project_root
    
    def __getConcreteClassFileName(self):
        """
        Returns file name of the concrete class.
        """
        my_class_file_path = inspect.getfile(self.__class__)
        my_class_file_name = os.path.basename(my_class_file_path)
        if not my_class_file_name:
            raise RuntimeError("Unable to determine the file name of the concrete class.")
        self._script_file_name = my_class_file_name
        return self._script_file_name
    
    def __getConcreteClassName(self):
        """
        Determines the Class name associated with the concrete class dynamically.
        """        
        my_class_class_name = self.__class__.__name__
        if not my_class_class_name:
            raise RuntimeError("Unable to determine the class name of the concrete class.")
        self._concrete_class_name = my_class_class_name        
        return self._concrete_class_name
    
    def __getConcreteClassDirectory(self):
        """
        Determines the directory of the concrete class dynamically.
        """        
        class_file_path = inspect.getfile(self.__class__)
        class_directory = os.path.dirname(class_file_path)
        if not class_directory:
            raise RuntimeError("Unable to determine the directory of the concrete class.")
        self._script_directory = class_directory

        return self._script_directory
    
    def __getConcreteClassAbsPath(self):
        """
        Returns file path of the concrete class.
        """
        my_class_file_path = inspect.getfile(self.__class__)
        if not my_class_file_path:
            raise RuntimeError("Unable to determine the path of the concrete class.")
        self._script_path = my_class_file_path
        return self._script_path

    def __getConfigFileName(self):
        """
        Private method to get the configuration file name.

        This method sets the CONFIG_FILENAME attribute to "config.yaml" and returns it.

        Returns:
            str: The name of the configuration file.
        """
        self.CONFIG_FILENAME = "config.yaml"
        return self.CONFIG_FILENAME

    def __initializeLogger(self):
        """
        Initializes the logger for the class instance.
        This method creates an instance of LoggerManager and assigns it to the 
        instance variable `__logger`.\n\n
        Returns:
            LoggerManager: The initialized logger instance.
        """

        self.__logger = LoggerManager()
        return self.__logger

    def __loadConfiguration(self):
        """
        Loads the configuration from the specified configuration path.
        This method uses the ConfigurationHelper class to load the configuration
        from the path defined in the CONFIG_PATH attribute. The loaded configuration
        is then stored in the __configuration attribute.\n\n
        Returns:
            dict: The loaded configuration.
        """

        self.__configuration = ConfigurationHelper().loadConfiguration(self.CONFIG_PATH)
        return self.__configuration
    
    async def _run(self):
        """
        Asynchronously runs the elaboration process within an event loop.
        This method attempts to get the current running event loop. If no event loop is running,
        it creates a new event loop and sets it as the current event loop. It then creates and
        awaits a task for the `elaboration` method.\n\n
        Raises:
            RuntimeError: If an error occurs during the process execution, it raises a RuntimeError
                          with the original exception message.
        """

        try:
            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            
            task = loop.create_task(self.elaboration())
            await task       
        except Exception as e:
            raise RuntimeError("Error during the process execution: %s", e) 
