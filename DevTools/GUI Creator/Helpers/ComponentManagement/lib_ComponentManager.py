from typing import Any, Dict

class ComponentManager:

    def __init__(self):
        self.components = {}

    def updateComponents(self, settings: Dict[str, Any]) -> None:
        """
        Aggiorna i componenti con i valori calcolati.
        settings: Dizionario con valori e formule.
        """
        for key, item in settings.items():
            if isinstance(item, dict):
                if 'value' in item and item['value'] is not None:
                    self.components[key] = item['value']
                elif isinstance(item, dict):
                    self.updateComponents(item)

    def getComponents(self) -> Dict[str, Any]:
        """Ritorna i componenti aggiornati."""
        return self.components