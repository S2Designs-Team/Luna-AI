from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

class Canvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: lightgray; border: 1px solid black;")
        self.setMinimumSize(400, 300)