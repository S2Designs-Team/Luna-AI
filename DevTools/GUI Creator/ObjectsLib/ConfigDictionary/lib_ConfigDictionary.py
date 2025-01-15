from typing import Any

class ConfigDictionary(dict):

    def getProperty_OLD(self, path: str) -> Any:
        """
        Retrieves the value of a nested property through a specific path.
        :param path: Dot-separated path, e.g., "main_window.width".
        :return: The value of the property.
        """
        keys = path.lower().split('.')
        current = self
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                raise KeyError(f"Proprietà non trovata: {path}")
        # Return the value if it exists, otherwise the dictionary itself
        return current['value'] if isinstance(current, dict) and 'value' in current else current
    
    def getProperty(self, path: str) -> Any:
        """
        Retrieves the value of a nested property through a specific path.
        If the value is a formula, attempts to resolve it.
        :param path: Dot-separated path, e.g., "main_window.width".
        :return: The value of the property.
        """
        keys = path.lower().split('.')
        current = self

        # Follow the path and access the property
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                raise KeyError(f"Property not found: {path}")

        # If the property has a formula, try to resolve it
        if isinstance(current, dict) and 'formula' in current:
            formula = current['formula']
            # If the formula is a string, we can attempt to resolve it as a formula
            if isinstance(formula, str) and '{' in formula and '}' in formula:
                # Resolve the formula, for example with a simple eval (a custom parser might be needed)
                resolved_value = self.resolve_formula(formula)
                return resolved_value
            # If the formula is a list of strings, attempt to resolve them
            elif isinstance(formula, list):
                return [self.resolve_formula(f) for f in formula]
        # Return the value if there is no formula
        return current['value'] if isinstance(current, dict) else current

    def resolve_formula(self, formula: str) -> Any:
        """
        Resolves a dynamic formula. Here you can add the logic to calculate or resolve formulas.
        For example, replace variables in the format {variable} with real values.
        """
        # Implement the logic to resolve formulas, for example:
        # 1. Replace variables in the format {variable} with actual values
        # 2. Use eval() or another approach to calculate the value if necessary
        # Here is a basic example of variable substitution
        if '{' in formula and '}' in formula:
            # Replace the variable with the value from the dictionary, if available
            formula = formula.strip('{}')  # Rimuove le parentesi
            if formula in self.__settings:
                return self.getProperty(formula)  # Returns the resolved value
            else:
                return formula  # Returns the raw formula if not found
        return formula  # Returns the formula if it is not modifiable

    def setProperty(self, path: str, value: Any):
        """
        Sets the value of a nested property through a specific path.
        :param path: Dot-separated path, e.g., "main_window.width".
        :param value: Value to assign to the property.
        """
        keys = path.lower().split('.')
        current = self
        for key in keys[:-1]:
            if key not in current or not isinstance(current[key], dict):
                current[key] = ConfigDictionary()
            current = current[key]
        current[keys[-1]] = {'value': value, 'formula': None}

    def hasProperty(self, path: str) -> bool:
        """
        Checks if a property exists in the nested dictionary.
        :param path: Dot-separated path, e.g., "main_window.width".
        :return: True if the property exists, otherwise False.
        """
        try:
            self.get_property(path)
            return True
        except KeyError:
            return False
        
    def getFormula(self, path: str) -> Any:
        """
        Retrieves the formula associated with a property, if it exists.
        """
        keys = path.lower().split('.')
        current = self
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                raise KeyError(f"Property not found: {path}")
        
        return current['formula'] if isinstance(current, dict) and 'formula' in current else None