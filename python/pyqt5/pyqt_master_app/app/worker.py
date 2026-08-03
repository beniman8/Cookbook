from PyQt5.QtCore import QThread, pyqtSignal
import time

class Worker(QThread):
    progress = pyqtSignal(int)
    def run(self):
        for i in range(101):
            time.sleep(0.05)
            self.progress.emit(i)
