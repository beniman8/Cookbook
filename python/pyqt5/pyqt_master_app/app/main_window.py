from PyQt5.QtWidgets import *
from python.pyqt5.pyqt_master_app.app.theme import apply_dark, apply_light
from python.pyqt5.pyqt_master_app.ui.dashboard import Dashboard
from python.pyqt5.pyqt_master_app.ui.table_view import TableViewWidget
from python.pyqt5.pyqt_master_app.ui.drag_drop import DragDropWidget
from python.pyqt5.pyqt_master_app.ui.charts import ChartWidget
from python.pyqt5.pyqt_master_app.app.state_manager import save_state, load_state

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Master App")
        self.resize(1200, 800)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tabs.addTab(Dashboard(), "Dashboard")
        self.tabs.addTab(TableViewWidget(), "Table")
        self.tabs.addTab(DragDropWidget(), "Drag & Drop")
        self.tabs.addTab(ChartWidget(), "Charts")

        self.create_menu()
        apply_dark(self)

    def create_menu(self):
        menu = self.menuBar()

        theme_menu = menu.addMenu("Theme")
        theme_menu.addAction("Dark", lambda: apply_dark(self))
        theme_menu.addAction("Light", lambda: apply_light(self))

        file_menu = menu.addMenu("File")
        file_menu.addAction("Save", self.save)
        file_menu.addAction("Load", self.load)

    def save(self):
        save_state({"tab": self.tabs.currentIndex()})

    def load(self):
        state = load_state()
        self.tabs.setCurrentIndex(state.get("tab", 0))
