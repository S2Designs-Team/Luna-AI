# EditorComponents/StatusBar/lib_StatusBar.py
from PyQt5.QtWidgets import QStatusBar, QLabel

class MainStatusBar(QStatusBar):

    _LBL_message:QLabel    = None

    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Elementi della status bar
        self._LBL_message:QLabel  = QLabel("Ready")
        self.addWidget(self._LBL_message)

        # Puoi aggiungere altri widget se necessario
        # esempio: un'icona di stato o un indicatore di progresso
        # self.progress_bar = QProgressBar()
        # self.addPermanentWidget(self.progress_bar)

    def setMessage(self, message: str, timeout: int = 0):
        """Imposta il messaggio della status bar."""
        self._LBL_message.setText(message)
        if timeout > 0:
            self.showMessage(message, timeout)
        else:
            self.showMessage(message)

    def clearMessage(self):
        """Cancella il messaggio della status bar."""
        super().clearMessage()
        self._LBL_message.setText("Ready")