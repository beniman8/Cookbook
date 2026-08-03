import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# ------------------------
# DRAGGABLE WIDGET
# ------------------------
class DraggableWidget(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setMinimumSize(80, 40)
        self.setStyleSheet("background:#3a86ff;color:white;border-radius:5px;")
        self.setMouseTracking(True)

        self.dragging = False
        self.offset = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(self.mapToParent(event.pos() - self.offset))

    def mouseReleaseEvent(self, event):
        self.dragging = False


# ------------------------
# DESIGN CANVAS
# ------------------------
class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background:#2b2b3c;")
        self.setAcceptDrops(True)
        self.selected = None

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        widget_type = event.mimeData().text()
        widget = self.create_widget(widget_type)
        widget.move(event.pos())
        widget.show()

    def create_widget(self, widget_type):
        if widget_type == "Button":
            w = DraggableWidget("Button", self)
        elif widget_type == "Label":
            w = QLabel("Label", self)
            w.setStyleSheet("color:white;")
        elif widget_type == "Input":
            w = QLineEdit(self)
        else:
            w = DraggableWidget("Widget", self)

        w.setParent(self)
        w.show()
        return w


# ------------------------
# PALETTE (LEFT SIDE)
# ------------------------
class Palette(QListWidget):
    def __init__(self):
        super().__init__()
        self.addItems(["Button", "Label", "Input"])

    def startDrag(self, *args):
        item = self.currentItem()
        if not item:
            return

        drag = QDrag(self)
        mime = QMimeData()
        mime.setText(item.text())

        drag.setMimeData(mime)
        drag.exec_()


# ------------------------
# PROPERTY PANEL
# ------------------------
class PropertyEditor(QWidget):
    def __init__(self):
        super().__init__()
        layout = QFormLayout()

        self.text = QLineEdit()
        self.text.textChanged.connect(self.update_text)

        layout.addRow("Text:", self.text)
        self.setLayout(layout)

        self.current_widget = None

    def set_widget(self, widget):
        self.current_widget = widget
        if isinstance(widget, (QPushButton, QLabel)):
            self.text.setText(widget.text())

    def update_text(self, value):
        if self.current_widget:
            if hasattr(self.current_widget, "setText"):
                self.current_widget.setText(value)


# ------------------------
# MAIN WINDOW
# ------------------------
class Builder(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt GUI Builder")
        self.resize(1200, 700)

        # Layout
        main = QWidget()
        layout = QHBoxLayout()

        self.palette = Palette()
        self.canvas = Canvas()
        self.props = PropertyEditor()

        layout.addWidget(self.palette, 1)
        layout.addWidget(self.canvas, 4)
        layout.addWidget(self.props, 1)

        main.setLayout(layout)
        self.setCentralWidget(main)

        self.canvas.mousePressEvent = self.select_widget

        self.create_menu()

    def select_widget(self, event):
        widget = self.canvas.childAt(event.pos())
        if widget:
            self.props.set_widget(widget)

    # ------------------------
    # EXPORT FEATURE
    # ------------------------
    def create_menu(self):
        menu = self.menuBar()
        file_menu = menu.addMenu("File")

        export = QAction("Export UI", self)
        export.triggered.connect(self.export_ui)

        file_menu.addAction(export)

    def export_ui(self):
        code = "from PyQt5.QtWidgets import *\n\n"
        code += "app = QApplication([])\nwindow = QWidget()\n\n"

        for child in self.canvas.children():
            if isinstance(child, QWidget):
                geo = child.geometry()
                code += f"{child.__class__.__name__}('{getattr(child, 'text', lambda:'' )()}').move({geo.x()},{geo.y()})\n"

        code += "\nwindow.show()\napp.exec_()"

        with open("generated_ui.py", "w") as f:
            f.write(code)

        QMessageBox.information(self, "Export", "UI exported!")


# ------------------------
# RUN
# ------------------------
app = QApplication(sys.argv)
window = Builder()
window.show()
sys.exit(app.exec_())