import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# ------------------------
# GLOBAL STYLES
# ------------------------
DARK_THEME = """
QMainWindow {
    background-color: #1e1e2f;
}

QLabel {
    color: #ffffff;
    font-size: 14px;
}

QPushButton {
    background-color: #3a86ff;
    color: white;
    border-radius: 8px;
    padding: 6px;
}
QPushButton:hover {
    background-color: #265df2;
}

QLineEdit, QTextEdit, QComboBox, QSpinBox {
    background-color: #2b2b3c;
    color: white;
    border: 1px solid #444;
    padding: 5px;
    border-radius: 6px;
}

QTableWidget {
    background-color: #2b2b3c;
    color: white;
    gridline-color: #444;
}

QHeaderView::section {
    background-color: #3a3a4f;
    color: white;
    padding: 5px;
}
"""

LIGHT_THEME = """
QMainWindow {
    background-color: #f5f5f5;
}
"""

# ------------------------
# CUSTOM WIDGET
# ------------------------
class ColorButton(QPushButton):
    def __init__(self):
        super().__init__("Pick Color")
        self.clicked.connect(self.pick_color)

    def pick_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.setStyleSheet(f"background-color: {color.name()};")


# ------------------------
# MAIN WINDOW
# ------------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Advanced GUI Playground")
        self.resize(1200, 800)

        self.setStyleSheet(DARK_THEME)

        self.init_ui()

    # ------------------------
    # UI SETUP
    # ------------------------
    def init_ui(self):
        self.create_menu()
        self.create_toolbar()
        self.create_statusbar()

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tabs.addTab(self.create_form_tab(), "Form")
        self.tabs.addTab(self.create_table_tab(), "Table")
        self.tabs.addTab(self.create_tree_tab(), "Tree")
        self.tabs.addTab(self.create_controls_tab(), "Controls")

        self.create_dock()

    # ------------------------
    # MENU
    # ------------------------
    def create_menu(self):
        menu = self.menuBar()

        file_menu = menu.addMenu("File")

        open_action = QAction("Open File", self)
        open_action.triggered.connect(self.open_file)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(open_action)
        file_menu.addAction(exit_action)

        theme_menu = menu.addMenu("Theme")

        dark = QAction("Dark", self)
        dark.triggered.connect(lambda: self.setStyleSheet(DARK_THEME))

        light = QAction("Light", self)
        light.triggered.connect(lambda: self.setStyleSheet(LIGHT_THEME))

        theme_menu.addAction(dark)
        theme_menu.addAction(light)

    # ------------------------
    # TOOLBAR
    # ------------------------
    def create_toolbar(self):
        toolbar = self.addToolBar("Main Toolbar")

        btn = QAction("Click Me", self)
        btn.triggered.connect(lambda: self.statusBar().showMessage("Toolbar clicked"))

        toolbar.addAction(btn)

    # ------------------------
    # STATUS BAR
    # ------------------------
    def create_statusbar(self):
        self.statusBar().showMessage("Ready")

    # ------------------------
    # DOCK
    # ------------------------
    def create_dock(self):
        dock = QDockWidget("Logs", self)
        self.log_box = QTextEdit()
        dock.setWidget(self.log_box)
        self.addDockWidget(Qt.BottomDockWidgetArea, dock)

    # ------------------------
    # FORM TAB
    # ------------------------
    def create_form_tab(self):
        widget = QWidget()
        layout = QFormLayout()

        self.name_input = QLineEdit()
        self.age_input = QSpinBox()
        self.gender = QComboBox()
        self.gender.addItems(["Male", "Female", "Other"])

        submit = QPushButton("Submit")
        submit.clicked.connect(self.submit_form)

        layout.addRow("Name:", self.name_input)
        layout.addRow("Age:", self.age_input)
        layout.addRow("Gender:", self.gender)
        layout.addRow(submit)

        widget.setLayout(layout)
        return widget

    def submit_form(self):
        name = self.name_input.text()
        age = self.age_input.value()
        gender = self.gender.currentText()

        self.log_box.append(f"User: {name}, {age}, {gender}")

    # ------------------------
    # TABLE TAB
    # ------------------------
    def create_table_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        self.table = QTableWidget(5, 3)
        self.table.setHorizontalHeaderLabels(["Name", "Age", "Country"])

        for row in range(5):
            for col in range(3):
                self.table.setItem(row, col, QTableWidgetItem(f"Item {row},{col}"))

        layout.addWidget(self.table)
        widget.setLayout(layout)
        return widget

    # ------------------------
    # TREE TAB
    # ------------------------
    def create_tree_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        tree = QTreeWidget()
        tree.setHeaderLabels(["Category", "Items"])

        parent = QTreeWidgetItem(tree, ["Fruits"])
        QTreeWidgetItem(parent, ["Apple"])
        QTreeWidgetItem(parent, ["Banana"])

        layout.addWidget(tree)
        widget.setLayout(layout)
        return widget

    # ------------------------
    # CONTROLS TAB
    # ------------------------
    def create_controls_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        slider = QSlider(Qt.Horizontal)
        slider.valueChanged.connect(lambda v: self.statusBar().showMessage(f"Slider: {v}"))

        progress = QProgressBar()
        slider.valueChanged.connect(progress.setValue)

        checkbox = QCheckBox("Enable something")
        checkbox.stateChanged.connect(lambda s: self.log_box.append(f"Checkbox: {s}"))

        color_btn = ColorButton()

        layout.addWidget(slider)
        layout.addWidget(progress)
        layout.addWidget(checkbox)
        layout.addWidget(color_btn)

        widget.setLayout(layout)
        return widget

    # ------------------------
    # FILE DIALOG
    # ------------------------
    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File")
        if file_name:
            self.log_box.append(f"Opened: {file_name}")


# ------------------------
# RUN APP
# ------------------------
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())