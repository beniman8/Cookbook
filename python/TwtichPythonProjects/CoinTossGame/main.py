import sys 
from random import choice 




from PyQt5.QtWidgets import(
    QMainWindow,
    QApplication,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QWidget
)


from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt 

SCREEN_WIDTH,SCREEN_HEIGHT = 800,800


class CoinToss(QMainWindow):
    def __init__(self,screen_width,screen_height ):
        super().__init__()
        self.setWindowTitle("COIN TOSS")
        self.setGeometry(int(screen_width/3),int(screen_height/3),SCREEN_WIDTH,SCREEN_HEIGHT)
        
        self.initUI()
        
        
    def initUI(self):
        
        # main layout 
        main_layout = QVBoxLayout()
        
        
        #label 
        self.label = QLabel("HEADS or TAILS")
        self.label.setFont(QFont("Arial",100))
        self.label.setAlignment(Qt.AlignCenter)
        
        # button 
        self.button = QPushButton("Flip the Coin")
        
        
        self.button.setStyleSheet("""
                                QPushButton{
                                    font-size:18px;
                                    color:blue;
                                }
                                
                                
                                """)
        
        self.button.clicked.connect(self.flipTheCoin)
        
        
        # add widget to screen 
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.button)
        
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)


    def flipTheCoin(self):
        
        face = ["HEADS","TAILS"]
        res = choice(face)
        
        self.label.setText(str(res))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    screen_geometry = screen.size()
    screen_width , screen_height = screen_geometry.width(),screen_geometry.height()

    window = CoinToss(screen_width,screen_height)
    window.show()
    
    sys.exit(app.exec_())
