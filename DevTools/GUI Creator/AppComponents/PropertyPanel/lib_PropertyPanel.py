from PyQt5.QtWidgets import QDockWidget, QVBoxLayout, QWidget, QLabel, QLineEdit, QTableWidget, QTableWidgetItem

class PropertyPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        self.table = QTableWidget(self)
        self.layout.addWidget(self.table)

    def updateProperties(self, component):
        """Aggiorna il pannello delle proprietà per visualizzare le proprietà del componente selezionato"""
        self.table.clear()
        self.table.setRowCount(0)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Property", "Value"])
        #print(component)

        meta_object = component.metaObject()
        for i in range(meta_object.propertyCount()):
            prop = meta_object.property(i)
            prop_name = prop.name()
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem(prop_name))
            value = component.property(prop_name)
            if isinstance(value, str):
                editor = QLineEdit(value)
                editor.editingFinished.connect(lambda prop_name=prop_name, editor=editor: component.setProperty(prop_name, editor.text()))
                self.table.setCellWidget(i, 1, editor)
            else:
                self.table.setItem(i, 1, QTableWidgetItem(str(value)))