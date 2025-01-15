import yaml
import os
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class PreferencesWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Preferences")
        self.setGeometry(200, 200, 400, 300)

        # Layout della finestra delle preferenze
        self.layout = QVBoxLayout(self)    

        self.config_file = os.path.join("config", "settings.yaml")

        # Layout della finestra
        self.create_widgets()

        # Carica le impostazioni attuali
        self.load_settings()

    def create_widgets(self):
        self.layout.addWidget(QLabel("Editor Background Color:"))
        self.bg_color_input = QLineEdit(self)
        self.layout.addWidget(self.bg_color_input)

        self.layout.addWidget(QLabel("Grid Size:"))
        self.grid_size_input = QLineEdit(self)
        self.layout.addWidget(self.grid_size_input)

        save_button = QPushButton("Save", self)
        save_button.clicked.connect(self.save_settings)
        self.layout.addWidget(save_button)

    def load_settings(self):
        """Carica le impostazioni da file."""
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as f:
                settings = yaml.safe_load(f)
                self.grid_size_input.text = settings.get("grid_size", 20)
                self.bg_color_input.text  = settings.get("background_color", 20)

    def save_settings(self):
        """Salva le impostazioni nel file YAML."""
        bg_color  = self.bg_color_input.text()
        grid_size = self.grid_size_input.text()

        settings = {
            "grid_size":         grid_size,
            "background_color" : bg_color
        }

        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        with open(self.config_file, "w") as f:
            yaml.safe_dump(settings, f)

        print(f"Preferences saved: Background Color = {bg_color}, Grid Size = {grid_size}")

        self.window.destroy()