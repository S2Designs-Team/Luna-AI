from PyQt5.QtWidgets import QLabel, QFrame, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QColor, QMouseEvent
from .lib_Position import Position
from .lib_Size import Size
from .lib_Border import Border
from .lib_UIElement import UIElement

class UIWindow(UIElement):
    def __init__(self, par_parent=None):
        super().__init__(par_parent)
        self.setObjectName("UIWindow")
        
        # Configurazioni di default per la finestra
        self.borders = Border(2, QColor("black"))
        self.setSize(400, 300)
        self.setStyleSheet("""
            #UIWindow {
                background-color: white;
                border: 2px solid black;
                border-radius: 10px;
            }
        """)

        # Layout principale
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Barra del titolo
        self.title_bar = UITitleBar(self, title="UI Window")
        self.layout.addWidget(self.title_bar)

        # Area centrale
        self.__create_content_area()

    def __create_content_area(self):
        """Crea l'area centrale per i sottocomponenti."""
        self.content_area = QFrame(self)
        self.content_area.setObjectName("ContentArea")
        self.content_area.setStyleSheet("""
            #ContentArea {
                background-color: #f9f9f9;
                border-bottom-left-radius: 10px;
                border-bottom-right-radius: 10px;
            }
        """)
        self.content_area.setLayout(QVBoxLayout())
        self.layout.addWidget(self.content_area)

    def add_child_to_content(self, child: UIElement):
        """Aggiunge un sottocomponente all'area centrale."""
        self.content_area.layout().addWidget(child)