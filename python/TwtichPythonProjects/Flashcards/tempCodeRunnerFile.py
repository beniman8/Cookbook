import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QTabWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 QTabWidget Example")
        self.setGeometry(300, 200, 500, 300)

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        self.tabs = QTabWidget()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tabs.addTab(self.tab1, "Home")
        self.tabs.addTab(self.tab2, "Settings")
        self.tabs.addTab(self.tab3, "About")

        self.create_home_tab()
        self.create_settings_tab()
        self.create_about_tab()

        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

    def create_home_tab(self):
        layout = QVBoxLayout()

        label = QLabel("Welcome to the Home Tab")
        button = QPushButton("Click Me")

        layout.addWidget(label)
        layout.addWidget(button)

        self.tab1.setLayout(layout)

    def create_settings_tab(self):
        layout = QVBoxLayout()

        label = QLabel("Settings Tab")
        input_box = QLineEdit()
        input_box.setPlaceholderText("Enter your name")

        layout.addWidget(label)
        layout.addWidget(input_box)

        self.tab2.setLayout(layout)

    def create_about_tab(self):
        layout = QVBoxLayout()

        label = QLabel("This is a simple PyQt5 app using QTabWidget.")

        layout.addWidget(label)

        self.tab3.setLayout(layout)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())