from PyQt5.QtWidgets import *
from python.pyqt5.pyqt_master_app.app.worker import Worker

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.bar = QProgressBar()
        btn = QPushButton("Start Task")

        btn.clicked.connect(self.run)

        layout.addWidget(self.bar)
        layout.addWidget(btn)
        self.setLayout(layout)

    def run(self):
        self.worker = Worker()
        self.worker.progress.connect(self.bar.setValue)
        self.worker.start()
