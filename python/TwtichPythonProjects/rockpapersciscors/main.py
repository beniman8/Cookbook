import sys 

import random


WORDS = ('rock','paper','scissors')

RELATIONSHIP= {'rock':'scissors','paper':'rock','scissors':'paper'}


from PyQt5.QtWidgets import (
    
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
)



class RockPaperScissors(QWidget):
    
    def __init__(self):
        super().__init__()
        
        
        self.initUI()
        
        
    def initUI(self):
        self.setWindowTitle("ROCK PAPER SCISSORS")
        
        main_layout = QVBoxLayout()
        
        #display 
        self.display = QLabel("CHOOSE ROCK PAPER OR SCISSORS")
        
        
        #buttons 
        
        self.rock = QPushButton("ROCK")
        self.paper = QPushButton("PAPER")
        self.scissors = QPushButton("SCISSORS")
        
        main_layout.addWidget(self.display)
        
        
        main_layout.addWidget(self.rock)
        main_layout.addWidget(self.paper)
        main_layout.addWidget(self.scissors)
        
        
        self.rock.clicked.connect(lambda: self.generate_answer("rock"))
        self.paper.clicked.connect(lambda: self.generate_answer("paper"))
        self.scissors.clicked.connect(lambda: self.generate_answer("scissors"))
        
        
        self.setLayout(main_layout)
        
        
        self.setStyleSheet(
            
            
            """
            QPushButton,QLabel{
                padding:20px;
                
                font-weight:bold;
                font-family:calibri;
            }
            QPushButton{
                font-size:50px;
            }
            QLabel{
                font-size:120px;
                
                background-color:blue;
                
                border-radius:20px;
            }
            
            
            """
            
        )
        
    def generate_answer(self,answer):
        computer_choice = random.choice(WORDS)
        
        if computer_choice == answer:
            self.display.setText(f"Tie Game : computer -> {computer_choice}")
            
        elif RELATIONSHIP[answer] == computer_choice:
            self.display.setText(f"YOU WON : computer -> {computer_choice}")
            
        else:
            self.display.setText(f"You Lost: computer -> {computer_choice}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    rps = RockPaperScissors()
    

    rps.show()
    

    sys.exit(app.exec_())
    