import os
from pydantic import ConfigDict
import yaml
from typing import Any, Dict
from ObjectsLib.ConfigDictionary.lib_ConfigDictionary import ConfigDictionary

class ConfigurationManager():
    __yaml_file:str = None
    __settings      = ConfigDictionary()

    #- [CONSTRUCTOR] ----------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------
    def __init__(self, par_config_path:str=None):
        """
        """
        try: 
            self.yaml = yaml
            if par_config_path:
                self.loadYaml(par_config_path)
        except Exception as e:
            raise RuntimeError(f"{e}")
   
    #- [EXPOSED METHODS] ------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------
    def loadYaml(self, par_config_path:str=None) -> ConfigDictionary:
        try:
            if par_config_path:
                self.__checkConfigFile(par_config_path)
                self.__yaml_file = par_config_path

            with open(self.__yaml_file, 'r') as file:
                my_raw_data = yaml.safe_load(file)
                self.__settings = self.__processConfig(my_raw_data)

            return self.__settings
        
        except Exception as e:
            raise RuntimeError(f"{e}")
        
    def saveConfiguration(self, par_config_path):
        """
        Salva il contenuto di settings in un file YAML.
        Se una proprietà ha una formula, salva la formula; altrimenti salva il valore.
        """
        output_file = output_file or self.yaml_file
        data_to_save = self.__convertToYamlFormat(self.settings)

        with open(output_file, 'w') as file:
            yaml.dump(data_to_save, file, default_flow_style=False)

    #- [PRIVATE METHODS] ------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------
    def __processConfig(self, data: Dict[str, Any], parent_key: str = '') -> ConfigDictionary:
        """Elabora il contenuto del file YAML, salvando le formule come stringhe."""
        my_resulting_read_settings = ConfigDictionary()

        for key, value in data.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            full_key = full_key.lower()

            if isinstance(value, str) and ('{' in value) and ('}' in value):

                # Formula non calcolata
                my_resulting_read_settings[key] = ConfigDictionary({'formula': value, 'value': None})  # Salva formula e valore
            
            elif isinstance(value, dict):

                # Ricorsione per gestire dizionari annidati
                my_processed_value = self.__processConfig(value, full_key)
                if not isinstance(my_processed_value, ConfigDictionary):
                    my_processed_value = ConfigDictionary(my_processed_value)
                my_resulting_read_settings[key] = my_processed_value                

            else:
                # Valore semplice
                my_resulting_read_settings[key] = ConfigDictionary({'formula': None, 'value': value})

        return my_resulting_read_settings

    def __checkConfigFile(self, par_config_path:str):
        if not os.path.exists(par_config_path):
            raise RuntimeError(f"Config file: '{par_config_path}' does not exist or has been removed. Please check it.")

    def __convertToConfigDictionary(self, data):
        if isinstance(data, dict):
            return ConfigDictionary({k: self.__convertToConfigDictionary(v) for k, v in data.items()})
        elif isinstance(data, list):
            return [self.__convertToConfigDictionary(item) for item in data]
        else:
            return data

    def __convertToYamlFormat(self, data: ConfigDictionary) -> dict:
        """
        Converte il ConfigDictionary in un dizionario adatto per essere serializzato in YAML.
        """
        converted = {}
        for key, value in data.items():
            if isinstance(value, ConfigDict):
                # Ricorsione per i dizionari annidati
                converted[key] = self._convert_to_yaml_format(value)
            elif isinstance(value, dict):
                # Salva la formula, se esiste, altrimenti il valore
                converted[key] = value['formula'] if value.get('formula') else value.get('value')
            else:
                # Valori semplici
                converted[key] = value
        return converted