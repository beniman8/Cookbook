import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem, QVBoxLayout, QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidget Store Two Items Example")
        
        layout = QVBoxLayout(self)
        self.list_widget = QListWidget(self)
        layout.addWidget(self.list_widget)
        
        # 1. Create a QListWidgetItem with a primary display label
        item = QListWidgetItem("Apple")
        
        # 2. Store two values (e.g., ID and extra metadata) using setData
        two_values = (101, "A sweet red fruit")
        item.setData(Qt.UserRole, two_values)
        
        self.list_widget.addItem(item)
        
        # Connect click event to retrieve the two stored values
        self.list_widget.itemClicked.connect(self.on_item_clicked)
        
    def on_item_clicked(self, item):
        # Retrieve the tuple using data()
        id_val, description = item.data(Qt.UserRole)
        print(f"Display Text: {item.text()}")
        print(f"Stored ID: {id_val}, Stored Description: {description}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())