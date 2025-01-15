from PyQt5.QtWidgets import QFileIconProvider, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTreeView, QListWidget, QFileSystemModel, QMessageBox, QSplitter, QComboBox, QListWidgetItem
from PyQt5.QtCore import Qt, QDir, QSize, QThread, pyqtSignal, QFileInfo
from PyQt5.QtGui import QIcon

class FileLoaderThread(QThread):
    files_loaded = pyqtSignal(list)

    def __init__(self, path, filters):
        super().__init__()
        self.path = path
        self.filters = filters

    def run(self):
        dir = QDir(self.path)
        entries = dir.entryList(QDir.NoDotAndDotDot | QDir.AllEntries)
        if self.filters:
            filtered_entries = [entry for entry in entries if any(QDir.match(f, entry) for f in self.filters)]
        else:
            filtered_entries = entries
        self.files_loaded.emit(filtered_entries)

class OpenFileDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Open File")
        self.setGeometry(200, 200, 800, 600)

        # Layout principale
        main_layout = QVBoxLayout(self)

        # AddressBar
        self.address_bar = QLineEdit(self)
        self.address_bar.setReadOnly(True)
        main_layout.addWidget(self.address_bar)

        # Splitter per TreeView e ListView
        splitter = QSplitter(Qt.Horizontal)

        # TreeView per la struttura del file system
        self.tree_view = QTreeView(self)
        self.tree_model = QFileSystemModel()
        self.tree_model.setRootPath(QDir.rootPath())
        self.tree_model.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Drives)
        self.tree_view.setModel(self.tree_model)
        self.tree_view.setRootIndex(self.tree_model.index(QDir.rootPath()))
        self.tree_view.clicked.connect(self.on_tree_view_clicked)
        self.tree_view.setHeaderHidden(True)  # Nasconde l'intestazione della colonna
        self.tree_view.setColumnHidden(1, True)  # Nasconde la colonna "Size"
        self.tree_view.setColumnHidden(2, True)  # Nasconde la colonna "Type"
        self.tree_view.setColumnHidden(3, True)  # Nasconde la colonna "Date Modified"
        splitter.addWidget(self.tree_view)

        # ListView per i file nella directory selezionata
        self.list_view = QListWidget(self)
        self.list_view.setViewMode(QListWidget.IconMode)
        self.list_view.setIconSize(QSize(64, 64))
        self.list_view.setResizeMode(QListWidget.Adjust)
        self.list_view.setUniformItemSizes(True)
        self.list_view.setGridSize(QSize(120, 120))  # Aumenta lo spazio tra le icone del 50%
        self.list_view.itemDoubleClicked.connect(self.on_list_view_double_clicked)
        splitter.addWidget(self.list_view)

        main_layout.addWidget(splitter)

        # Riga con label, combo box per il nome del file selezionato e combo box per i filtri
        file_selection_layout = QHBoxLayout()
        file_selection_layout.addWidget(QLabel("Selected file name:", self))

        self.file_name_combo_box = QComboBox(self)
        file_selection_layout.addWidget(self.file_name_combo_box)

        self.filter_combo_box = QComboBox(self)
        self.filter_combo_box.addItem("All files (*.*)")
        self.filter_combo_box.addItem("UI Project files (*.uiprj)")
        self.filter_combo_box.currentIndexChanged.connect(self.on_filter_changed)
        file_selection_layout.addWidget(self.filter_combo_box)

        main_layout.addLayout(file_selection_layout)

        # Pulsanti
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # Aggiunge uno spazio flessibile per spingere i pulsanti a destra
        self.open_button = QPushButton("Apri", self)
        self.open_button.setEnabled(False)
        self.open_button.clicked.connect(self.open_file)
        button_layout.addWidget(self.open_button)

        self.cancel_button = QPushButton("Annulla", self)
        self.cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(self.cancel_button)

        main_layout.addLayout(button_layout)

    def on_tree_view_clicked(self, index):
        """Gestisce il click sulla TreeView"""
        path = self.tree_model.filePath(index)
        self.address_bar.setText(path)
        self.load_files_in_background(path)

    def on_list_view_double_clicked(self, item):
        """Gestisce il doppio click sulla ListView"""
        path = QDir(self.address_bar.text()).filePath(item.text())
        if QDir(path).exists():
            self.address_bar.setText(path)
            self.load_files_in_background(path)
            self.select_tree_view_item(path)

    def select_tree_view_item(self, path):
        """Seleziona l'elemento nella TreeView corrispondente al percorso specificato"""
        index = self.tree_model.index(path)
        if index.isValid():
            self.tree_view.setCurrentIndex(index)
            self.tree_view.scrollTo(index)

    def load_files_in_background(self, path):
        """Carica i file in background e aggiorna la list view e la combo box"""
        filters = self.get_current_filters()
        self.file_loader_thread = FileLoaderThread(path, filters)
        self.file_loader_thread.files_loaded.connect(self.update_list_view_and_combo_box)
        self.file_loader_thread.start()

    def update_list_view_and_combo_box(self, entries):
        """Aggiorna la list view e la combo box con i nomi dei file e delle directory nella directory selezionata"""
        self.list_view.clear()
        self.file_name_combo_box.clear()
        icon_provider = QFileIconProvider()
        for entry in entries:
            item = QListWidgetItem(entry)
            item.setIcon(icon_provider.icon(QFileInfo(self.address_bar.text() + '/' + entry)))
            self.list_view.addItem(item)
            self.file_name_combo_box.addItem(entry)

    def on_filter_changed(self, index):
        """Gestisce il cambiamento del filtro di visualizzazione dei file"""
        self.load_files_in_background(self.address_bar.text())

    def get_current_filters(self):
        """Ottiene i filtri di visualizzazione dei file correnti"""
        filter_text = self.filter_combo_box.currentText()
        if filter_text == "All files (*.*)":
            return []
        elif filter_text == "UI Project files (*.uiprj)":
            return ["*.uiprj"]
        return []

    def open_file(self):
        """Apre il file selezionato"""
        file_name = self.file_name_combo_box.currentText()
        path = self.address_bar.text()
        file_path = QDir(path).filePath(file_name)
        if file_path.endswith(".uiprj"):
            QMessageBox.information(self, "File Aperto", f"File selezionato: {file_path}")
            self.accept()
        else:
            QMessageBox.warning(self, "Errore", "Seleziona un file con estensione .uiprj")