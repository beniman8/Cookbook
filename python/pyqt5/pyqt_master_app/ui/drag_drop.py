from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

class DragDropWidget(QLabel):
    def __init__(self):
        super().__init__("Drop Files Here")
        self.setAcceptDrops(True)
        self.setAlignment(Qt.AlignCenter)

    def dragEnterEvent(self,e): e.accept()

    def dropEvent(self,e):
        files=[u.toLocalFile() for u in e.mimeData().urls()]
        self.setText("\n".join(files))
