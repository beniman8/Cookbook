import sys 


from random import randint,choice



from PyQt5.QtWidgets import(
    QMainWindow,
    QApplication,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QLabel,
    QComboBox,
    
)

from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


SCREEN_WIDTH,SCREEN_HEIGHT = 800, 800
STARTING_POS_LEFT_RIGHT = 1500
STARTING_POS_UP_DOWN = 50



class NumberGuessing(QMainWindow):
    
    
    def __init__(self,sw,sh):
        super().__init__()
        self.setWindowTitle("NUMBER GUESSING GAME")
        self.setGeometry(int(sw/3),int(sh/3),SCREEN_WIDTH,SCREEN_HEIGHT)
        
        #TODO add this logic to the program
        self.difficulty = {
            "easy":10,
            "medium":50,
            "hard":100,
        }
        
        self.numbers = [str(num) for num in range(10)]
        self.chosen_number = choice(self.numbers)
        #TODO ADD difficulty  example 10 number or 100 numbers
        print(self.chosen_number)
        
        
        self.initUI()
        
        
    
    
    def initUI(self):
        
        
        
        #OUR MAIN LAYOUT
        main_layout = QVBoxLayout()
        
        
        #LABEL
        Title = QLabel("CAN YOU GUESS THE NUMBER?")
        Title.setFont(QFont("Arial",40))
        
        self.CurrentNumber = QLabel()
        self.CurrentNumber.setFont(QFont("Arial",40))
        
        self.CurrentNumber.setStyleSheet(
            "color:#292929;"
            "background-color: #6fdcf7;"
        )
        
        Title.setStyleSheet(
            "color:#292929;"
            "background-color: #6fdcf7;"
        )
        Title.setAlignment(Qt.AlignTop)
        
        #INPUT BOX 
        InputBox = QComboBox()
        InputBox.addItems(self.numbers)
        
        InputBox.currentTextChanged.connect(self.hello)
        
        InputBox.setStyleSheet(
        """
        QComboBox{
            font-size: 40px;
        }
        
        """
            
        )
        

        #ADDING WIDGET TO MAIN SCREEN
        
        main_layout.addWidget(Title)
        main_layout.addWidget(self.CurrentNumber)

        main_layout.addWidget(InputBox)

        
        
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        
        
    def hello(self,i):
        #compared the guessed  number to the chosen number
        #True
        if int(self.chosen_number)==int(i):
            self.CurrentNumber.setText(f"The number you have guessed is: {i} and it is the correct number")
        else:
            self.CurrentNumber.setText(f"The number you have guessed is: {i} and it is the wrong number")

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    screen_geometry = screen.size()
    sw,sh =screen_geometry.width(),screen_geometry.height()

    
    window = NumberGuessing(sw,sh)
    window.show()
    
    sys.exit(app.exec_())