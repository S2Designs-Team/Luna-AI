import asyncio
import multiprocessing
import os
import inspect
import logging
from abc                                                       import ABC, abstractmethod
import sys
from AssetsLibs.Helpers.LogManager.lib_LogManager              import LoggerManager
from AssetsLibs.Helpers.Configuration.lib_Configuration        import ConfigurationHelper
from AssetsLibs.Helpers.MessageLogManagement.lib_ProcessLogger import ProcessLogger  # Added import for ProcessLogger

class BasicProcess(ABC):

    #- [PRIVATE OBJECTS]
    #--------------------------------------------------------------------------------------------------
    __logger:ProcessLogger             = None   # Specific logger
    __process:multiprocessing.Process  = None   # Process object

    #- [PRIVATE FIELDS]
    #--------------------------------------------------------------------------------------------------
    __project_root:str                 = None   # Project root directory (Directory)
    __concrete_class_name:str          = None   # Concrete class name (ClassName)
    __script_directory:str             = None   # Directory of the script file (Directory)
    __script_file_name:str             = None   # File name of the concrete class script (FileName)
    __script_path:str                  = None   # Path of the script file (Directory + FileName)
    
    __config_directory:str             = None   # Configuration file directory (Directory)
    __config_file_name:str             = None   # Configuration file name (FileName)
    __config_path:str                  = None   # Configuration file path (Directory + FileName)
    __configuration:dict               = None   # Configuration of the concrete class (Dictionary)

    __is_process_initialized:bool      = False  # Process initialization flag
    
    @property
    def is_process_initialized(self):
        return self.__is_process_initialized
    @is_process_initialized.setter
    def is_process_initialized(self, value:bool):
        self.__is_process_initialized = value
    
    #- [PROPERTIES]
    #--------------------------------------------------------------------------------------------------
    @property
    def project_root(self):
        """
        Readonly Property: The full path of the application's entry point.
        """   
        return self.__project_root
    
    @property
    def class_name(self):
        """
        Readonly Property: The name of the concrete class.
        """
        return self.__concrete_class_name 

    @property
    def class_directory(self):
        """
        Readonly Property: The directory of the concrete class.
        """
        return self.__script_directory

    @property
    def class_path(self):
        """
        Readonly Property: The file path of the concrete class.
        """
        return self.__script_path
    
    @property
    def class_file_name(self):
        """
        Readonly Property: The file name of the concrete class.
        """
        return self.__script_file_name

    @property
    def configuration(self):
        return self.__configuration

    @property
    def config_directory(self):
        """
        Property: The configuration directory.\n\n
        If the configuration directory is not set,
        it is the script directory.
        """
        if not self.__config_directory:
            self.__config_directory = self.__script_directory
        return self.__config_directory
    @config_directory.setter
    def config_directory(self, value):
        """
        Args:
            value (str): The path to the configuration directory.
        Raises:
            TypeError: If the provided value is not a string.
        """
        if isinstance(value, str):
            self.__config_directory = value
            self.__config_path = os.path.join(self.config_directory, self.config_file_name)
        else:
            raise TypeError("The config_directory value must be string.")

    @property
    def config_file_name(self):
        """
        Property: The configuration File Name.
        """
        return self.__config_file_name
    @config_file_name.setter
    def config_file_name(self, value):
        """
        Args:
            value (str): The name of the configuration file.
        Raises:
            TypeError: If the provided value is not a string.
        """
        if isinstance(value, str):
            self.__config_file_name = value
            self.__config_path = os.path.join(self.config_directory, self.config_file_name)
        else:
            raise TypeError("The config_file_name value must be string.")   
       
    @property
    def config_path(self):
        """
        Readonly Property: The configuration File Path.
        """        
        return os.path.join(self.__config_path)
    
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
        raise NotImplementedError("[%s] Must implement the 'initialize' method.", self.class_name)
        pass
   
    @abstractmethod
    async def elaboration(self):
        """
        [Abstract Method - It must be implemented by concrete classes.]/\n
        Abstract Method to define the main elaboration logic for the concrete process.
        """
        raise NotImplementedError("[%s] Must implement the 'elaboration' method.", self.class_name)
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
            self.__project_root = os.path.dirname(os.path.abspath(main_module))

            # Verifica che la directory sia valida
            if not os.path.isdir(self.__project_root):
                raise RuntimeError(f"[BasicProcess]::[__getExcecutionRoot] => Invalid project root directory: {self.__project_root}")

        except Exception as e:
            raise RuntimeError(f"[BasicProcess]::[__getExcecutionRoot] => Error determining execution root: {e}")

        return self.__project_root
    
    def __getConcreteClassFileName(self):
        """
        Returns file name of the concrete class.
        """
        my_class_file_path = inspect.getfile(self.__class__)
        my_class_file_name = os.path.basename(my_class_file_path)
        if not my_class_file_name:
            raise RuntimeError(f"[BasicProcess]::[__getConcreteClassName] => Unable to determine the file name of the concrete class.")
        self.__script_file_name = my_class_file_name
        return self.__script_file_name
    
    def __getConcreteClassName(self):
        """
        Determines the Class name associated with the concrete class dynamically.
        """        
        my_class_class_name = self.__class__.__name__
        if not my_class_class_name:
            raise RuntimeError(f"[BasicProcess]::[__getConcreteClassName] => Unable to determine the class name of the concrete class.")
        self.__concrete_class_name = my_class_class_name        
        return self.__concrete_class_name
    
    def __getConcreteClassDirectory(self):
        """
        Determines the directory of the concrete class dynamically.
        """        
        my_class_file_path = inspect.getfile(self.__class__)
        my_class_directory = os.path.dirname(my_class_file_path)
        if not my_class_directory:
            raise RuntimeError(f"[BasicProcess]::[__getConcreteClassDirectory] => Unable to determine the directory of the concrete class.")
        self.__script_directory = my_class_directory

        return self.__script_directory
    
    def __getConcreteClassAbsPath(self):
        """
        Returns file path of the concrete class.
        """
        my_class_file_path = inspect.getfile(self.__class__)
        if not my_class_file_path:
            raise RuntimeError(f"[BasicProcess]::[__getConcreteClassAbsPath] => error occurred: Unable to determine the path of the concrete class.")
        self.__script_path = my_class_file_path
        return self.__script_path

    def __getConfigFileName(self):
        """
        Private method to get the configuration file name.

        This method sets the 'config_file_name' value to "config.yaml" and returns it.

        Returns:
            str: The name of the configuration file.
        """
        self.config_file_name = "config.yaml"
        return self.config_file_name

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
        try: 
            self.__configuration = ConfigurationHelper().loadConfiguration(self.config_path)
            return self.__configuration
        except Exception as e:
            raise RuntimeError(f"[BasicProcess]::[__loadConfiguration] => error occurred: {e.with_traceback}")
    
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
