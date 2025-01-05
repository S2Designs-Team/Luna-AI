import yaml
import os

class ConfigurationHelper():

    #- [CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        """
        self.yaml = yaml

    def loadConfiguration(self, par_config_path):
        """
        Carica un file `config.yaml` dalla directory specificata.
        
        :param par_config_path: The path of the configuration file.
        :return: A dictionary containing all the configuration parameters.
        """
        if not os.path.exists(par_config_path):
            # Restituisci un dizionario vuoto se il file non esiste
            return {}
        
        with open(par_config_path, "r") as file:
            return self.yaml.safe_load(file)
        
    def saveConfiguration(self, config_dir):
        """
        Salva il file `config.yaml` dalla directory specificata.
        
        :param config_dir: Directory contenente il file `config.yaml`.
        """
