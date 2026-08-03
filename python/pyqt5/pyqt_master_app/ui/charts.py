from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure

class ChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        fig = Figure()
        canvas = Canvas(fig)
        ax = fig.add_subplot(111)
        ax.plot([1,2,3],[10,20,15])
        layout.addWidget(canvas)
        self.setLayout(layout)
