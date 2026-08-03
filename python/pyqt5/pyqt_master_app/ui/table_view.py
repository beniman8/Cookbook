from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Model(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.data_list = [["Alice",25],["Bob",30]]

    def rowCount(self,i): return len(self.data_list)
    def columnCount(self,i): return 2

    def data(self,index,role):
        if role==Qt.DisplayRole:
            return self.data_list[index.row()][index.column()]

class TableViewWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        table = QTableView()
        table.setModel(Model())
        layout.addWidget(table)
        self.setLayout(layout)
