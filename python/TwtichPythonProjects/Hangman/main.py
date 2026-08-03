import sys  

from random import choice
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
from PyQt5.QtGui import QPixmap,QIcon

from PyQt5.QtWidgets import (
    
    QApplication,
    QWidget,
    QLabel,
    QComboBox,
    QVBoxLayout,
    
    
)




class HangMan(QWidget):
    
    def __init__(self):
        super().__init__()
        self.words = ["one","two","four"]
        self.letters = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","e","r","s","t","u","v","w","x","y","z"]
        self.guessed_letters = []
        self.guessed_wrong_letters = 0
        self.guessed_right_letters = 0

        
        
        self.initUI()
        
        
    def initUI(self):
        
        self.setWindowTitle("HANGMAN GAME BY BKG")
        self.setWindowIcon(QIcon("python/TwtichPythonProjects/Hangman/images/0.png"))
        self.setGeometry(500,100,800,800)
        
        #computer choice
        self.computer_choice = choice(self.words)
        
        #hint and hint space generator
        self.hint=""
        for _ in range(0,len(self.computer_choice)):
            self.hint +="_ "
            
        self.main_layout = QVBoxLayout()
        
        print(self.computer_choice)
        
        #IMAGE DISPLAY LABEL
        self.image_display = QLabel("Image")
        self.image_display.setPixmap(QPixmap(f"python/TwtichPythonProjects/Hangman/images/{self.guessed_wrong_letters}.png"))
        
        #WORD DISPLAY LABEL
        self.word_display = QLabel(self.hint)
        
        #LETTER SELECTION
        
        self.letter_selection = QComboBox()
        self.letter_selection.addItems(self.letters)
        
        
        self.main_layout.addWidget(self.image_display)
        self.main_layout.addWidget(self.word_display)
        self.main_layout.addWidget(self.letter_selection)
        
        self.letter_selection.currentTextChanged.connect(self.letter_selected)
        
        
        self.setLayout(self.main_layout)
        
        self.setStyleSheet(cozy_style)
        
    def letter_selected(self,letter):
        
     
        
        #Ignore the first empty letter 
        if letter == " ":
            return 
        
        self.guessed_letters.append(letter)
        
        # prevent combobox signal triggering that happens when i delete an item inside of it and try to use the combo box again
        self.letter_selection.blockSignals(True)
        
        
        #remove selected letter 
        current_index = self.letter_selection.currentIndex()    
        self.letter_selection.removeItem(current_index)
        
        self.letter_selection.blockSignals(False)
        
        
        display_word =""
        
        #increment the guess wrong
        if letter not in self.computer_choice:
            self.guessed_wrong_letters +=1
        else:
            self.guessed_right_letters +=1
            
        #can not have more than 8 errors
        if self.guessed_wrong_letters >= 8:
            
            self.guessed_wrong_letters =8
            
            
            
        for char in self.computer_choice:
            #you guessed right
            if char in self.guessed_letters:
                display_word += char + " "
            else:
                display_word +="_ "
                
        #update the image
        self.image_display.setPixmap(QPixmap(f"python/TwtichPythonProjects/Hangman/images/{self.guessed_wrong_letters}.png"))
        
        
        self.word_display.setText(display_word.capitalize())
        
        if self.guessed_right_letters == len(self.computer_choice):
            self.word_display.setText(f"You Won, the word was {self.computer_choice}".capitalize())
        elif self.guessed_wrong_letters == 8:
            self.word_display.setText(f"You lost the word was {self.computer_choice}".capitalize())

  
        
        
        
        
        
        
        
        
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    hangman = HangMan()
    
    hangman.show()
    
    sys.exit(app.exec_())
        
        
        
        
        
    