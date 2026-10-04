import stylesheet
from PyQt5.QtGui import QFont, QDoubleValidator
import sys  

from PyQt5 import QtWidgets


#Ignore the deprecation warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from helper import check_number

from stylesheet import (
    glass_style,
    dark_style,
    cyberpunk_style,
    cozy_style,
    neon_style,
    retro_style,
    scifi_style,
    minimal_style,
    
    )




from PyQt5.QtWidgets import (
    
    QApplication,
    QWidget,
    QLabel,
    QComboBox,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QTabWidget,
    QInputDialog,
    QGridLayout
    
    
)



class TicktacktoeGame(QWidget):

    def __init__(self):
        super().__init__()
        
        self.counter = 0
        
        self.buttons_with_x=""
        self.buttons_with_o=""
        
        

        self.initUI()
        
        
        self.display.setText('X it is your turn to play')
        


    def initUI(self):
        
        self.setWindowTitle("TICK TACK TOE")
        self.setGeometry(500,100,800,800)
        self.setStyleSheet(scifi_style)
        
        #layouts
        main_layout = QVBoxLayout()
        
        game_bt_layout = QGridLayout()
        
        label_layout = QVBoxLayout()
        
        play_reset_layout = QHBoxLayout()
        
        
        #Buttons
        
        self.play_reset_bt = QPushButton("PLAY/RESET")
        self.play_reset_bt.setStyleSheet("font-size: 50pt;")
        
        
        self.bt_0 = QPushButton("1")
        self.bt_1 = QPushButton("2")
        self.bt_2 = QPushButton("3")
        self.bt_3 = QPushButton("4")
        self.bt_4 = QPushButton("5")
        self.bt_5 = QPushButton("6")
        self.bt_6 = QPushButton("7")
        self.bt_7 = QPushButton("8")
        self.bt_8 = QPushButton("9")
        
        height,width = 250,250
        
        self.bt_0.setFixedSize(height,width)
        self.bt_1.setFixedSize(height,width)
        self.bt_2.setFixedSize(height,width)
        self.bt_3.setFixedSize(height,width)
        self.bt_4.setFixedSize(height,width)
        self.bt_5.setFixedSize(height,width)
        self.bt_6.setFixedSize(height,width)
        self.bt_7.setFixedSize(height,width)
        self.bt_8.setFixedSize(height,width)
        
        
        self.bt_0.setStyleSheet("font-size: 1pt;")
        self.bt_1.setStyleSheet("font-size: 1pt;")
        self.bt_2.setStyleSheet("font-size: 1pt;")
        self.bt_3.setStyleSheet("font-size: 1pt;")
        self.bt_4.setStyleSheet("font-size: 1pt;")
        self.bt_5.setStyleSheet("font-size: 1pt;")
        self.bt_6.setStyleSheet("font-size: 1pt;")
        self.bt_7.setStyleSheet("font-size: 1pt;")
        self.bt_8.setStyleSheet("font-size: 1pt;")
        
        
        #Labels
        self.display = QLabel()
        self.display.setFixedHeight(100)
        self.display.setStyleSheet("font-size: 30pt;")
        
        
        
        game_bt_layout.addWidget(self.bt_0, 0, 0)
        game_bt_layout.addWidget(self.bt_1, 0, 1)
        game_bt_layout.addWidget(self.bt_2, 0, 2)

        game_bt_layout.addWidget(self.bt_3, 1, 0)
        game_bt_layout.addWidget(self.bt_4, 1, 1)
        game_bt_layout.addWidget(self.bt_5, 1, 2)
        
        
        game_bt_layout.addWidget(self.bt_6, 2, 0)
        game_bt_layout.addWidget(self.bt_7, 2, 1)
        game_bt_layout.addWidget(self.bt_8, 2, 2)
        

        label_layout.addWidget(self.display)
        
        
        play_reset_layout.addWidget(self.play_reset_bt)
        
        
        
        main_layout.addLayout(game_bt_layout)
        main_layout.addLayout(label_layout)
        main_layout.addLayout(play_reset_layout)
        
        
        self.setLayout(main_layout)
        
        
        #Button Connected to Methods 
        self.bt_0.clicked.connect(lambda _:self.change_text(self.bt_0))
        self.bt_1.clicked.connect(lambda _:self.change_text(self.bt_1))
        self.bt_2.clicked.connect(lambda _:self.change_text(self.bt_2))
        self.bt_3.clicked.connect(lambda _:self.change_text(self.bt_3))
        self.bt_4.clicked.connect(lambda _:self.change_text(self.bt_4))
        self.bt_5.clicked.connect(lambda _:self.change_text(self.bt_5))
        self.bt_6.clicked.connect(lambda _:self.change_text(self.bt_6))
        self.bt_7.clicked.connect(lambda _:self.change_text(self.bt_7))
        self.bt_8.clicked.connect(lambda _:self.change_text(self.bt_8))
        
        
        self.play_reset_bt.clicked.connect(self.reset)





    def change_text(self, button):

        if self.counter % 2 == 0:
            self.current_letter = "X"
            self.buttons_with_x += button.text()
        else:
            self.current_letter = "O"
            self.buttons_with_o += button.text()

        button.setText(self.current_letter)
        button.setStyleSheet("font-size: 200pt;")
        button.setDisabled(True)

        self.counter += 1

        if check_number(self.buttons_with_x):
            self.display.setText("X has won the game")
            self.disable_all_buttons()
            return

        if check_number(self.buttons_with_o):
            self.display.setText("O has won the game")
            self.disable_all_buttons()
            return

        if self.counter == 9:
            self.display.setText("The game is a draw")
            return

        if self.counter % 2 == 0:
            self.display.setText("X it is your turn to play")
        else:
            self.display.setText("O it is your turn to play")
            
        
    def disable_all_buttons(self):
        self.bt_0.setDisabled(True)
        self.bt_1.setDisabled(True)
        self.bt_2.setDisabled(True)
        self.bt_3.setDisabled(True)
        self.bt_4.setDisabled(True)
        self.bt_5.setDisabled(True)
        self.bt_6.setDisabled(True)
        self.bt_7.setDisabled(True)
        self.bt_8.setDisabled(True)
        
            
    def reset(self):
        self.counter = 0
        self.buttons_with_x = ""
        self.buttons_with_o = ""

        self.bt_0.setText("1")
        self.bt_1.setText("2")
        self.bt_2.setText("3")
        self.bt_3.setText("4")
        self.bt_4.setText("5")
        self.bt_5.setText("6")
        self.bt_6.setText("7")
        self.bt_7.setText("8")
        self.bt_8.setText("9")

        self.bt_0.setEnabled(True)
        self.bt_1.setEnabled(True)
        self.bt_2.setEnabled(True)
        self.bt_3.setEnabled(True)
        self.bt_4.setEnabled(True)
        self.bt_5.setEnabled(True)
        self.bt_6.setEnabled(True)
        self.bt_7.setEnabled(True)
        self.bt_8.setEnabled(True)

        self.bt_0.setStyleSheet("font-size: 1pt;")
        self.bt_1.setStyleSheet("font-size: 1pt;")
        self.bt_2.setStyleSheet("font-size: 1pt;")
        self.bt_3.setStyleSheet("font-size: 1pt;")
        self.bt_4.setStyleSheet("font-size: 1pt;")
        self.bt_5.setStyleSheet("font-size: 1pt;")
        self.bt_6.setStyleSheet("font-size: 1pt;")
        self.bt_7.setStyleSheet("font-size: 1pt;")
        self.bt_8.setStyleSheet("font-size: 1pt;")

        self.display.setText("X it is your turn to play")
            











if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    game = TicktacktoeGame()
    
    
    game.show()
    
    sys.exit(app.exec_())
