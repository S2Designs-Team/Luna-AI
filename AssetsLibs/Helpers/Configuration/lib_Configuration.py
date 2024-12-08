import yaml
import os

class ConfigurationHelper():

    #- [CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        """
        self.yaml = yaml

    def loadConfiguration(self, config_dir):
        """
        Carica un file `config.yaml` dalla directory specificata.
        
        :param config_dir: Directory contenente il file `config.yaml`.
        :return: Dizionario con i parametri di configurazione.
        """
        config_path = os.path.join(config_dir, "config.yaml")
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configurazione non trovata: {config_path}")
        
        with open(config_path, "r") as file:
            return self.yaml.safe_load(file)
        
    def saveConfiguration(self, config_dir):
        """
        Salva il file `config.yaml` dalla directory specificata.
        
        :param config_dir: Directory contenente il file `config.yaml`.
        """
