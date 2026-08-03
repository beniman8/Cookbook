import sys 
from random import choice

from PyQt5.QtWidgets import(
    QMainWindow,
    QApplication,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QWidget,
)


from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

SCREEN_WIDTH,SCREEN_HEIGHT = 800,800

class DiceRoll(QMainWindow):

    def __init__(self,screen_width,screen_height):
        super().__init__()
        self.setWindowTitle("Dice Roller ")
        self.setGeometry(int(screen_width/3),int(screen_height/3),SCREEN_WIDTH,SCREEN_HEIGHT)

        self.initUI()

    def initUI(self):

        # main layout
        main_layout = QVBoxLayout()

        # Label
        self.label = QLabel("5")
        self.label.setFont(QFont("Arial",100))
        self.label.setAlignment(Qt.AlignCenter)

        # button
        self.button = QPushButton("Role The Dice ")

        self.button.setStyleSheet("""
                                QPushButton{
                                    font-size:18px;
                                    color:red;
                                    
                                    }
                                
                                """)
        self.button.clicked.connect(self.roleDice)

        # add widget to screen
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.button)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        
        
    def roleDice(self):
        
        dice = [1,2,3,4,5,6]
        value = choice(dice)
        #TODO ANIMATE THE DICE
        self.label.setText(str(value))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    screen_geometry = screen.size()
    screen_width ,screen_height = screen_geometry.width(),screen_geometry.height()
    
    
    window = DiceRoll(screen_width,screen_height)
    window.show()
    
    sys.exit(app.exec_())
