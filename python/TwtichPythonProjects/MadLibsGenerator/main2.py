import sys


from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QLabel,
    QGridLayout
)

from PyQt5.QtCore import Qt


class MadLibGenerator(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("MADLIBS GENERATOR")
        self.setGeometry(700, 300, 350, 450)


        self.initUI()

    def initUI(self):

        main_layout = QVBoxLayout()

        self.button = QPushButton("First MadLibs")

        self.button.setFixedSize(150,60)

        self.button.setStyleSheet("""
            QPushButton{
                font-size:18px;
                background:#2d2d2d;
                color:white;
                border-radius:10px;
            }

            QPushButton:hover{
                background:#3c3c3c;
            }

            QPushButton:pressed{
                background:#5a5a5a;
            }
        """)
        #button to function 
        self.button.clicked.connect(self.hello)
        
        
        main_layout.addWidget(self.button)

        widget = QWidget()
        widget.setLayout(main_layout)

        self.setCentralWidget(widget)

        # Dark window theme
        self.setStyleSheet("background:#121212;")
        
        
    def hello(self):
        hey = input('enter your name')
        
        print(f'{hey}')
        

    def madlib1(self):
        
        #TODO change all the inputs to self.line_edit = QLineEdit(self)  but find a cool way to generate the text field when the button is clicked
        animals= input('enter a animal name : ')
        profession = input('enter a profession name: ')
        cloth = input('enter a piece of cloth name: ')
        things = input('enter a thing name: ')
        name= input('enter a name: ')
        place = input('enter a place name: ')
        verb = input('enter a verb in ing form: ')
        food = input('food name: ')
        print(
            "say "
            + food
            + ", the photographer said as the camera flashed! "
            + name
            + " and I had gone to "
            + place
            + " to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as "
            + animals
            + " pretending to be a "
            + profession
            + ". when we saw the second photo, it was exactly what I wanted. We both looked like "
            + things
            + " wearing "
            + cloth
            + " and "
            + verb
            + " --exactly what I had in mind"
        )
        
def madlib2():

    adjactive = input('enter adjective : ')
    color = input('enter a color name : ')
    thing = input('enter a thing name :')
    place = input('enter a place name : ')
    person= input('enter a person name : ')
    adjective1 = input('enter a adjective : ')
    insect= input('enter a insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb name : ')
    
    print(
        "Last night I dreamed I was a "
        + adjective
        + " butterfly with "
        + color
        + " splotches that looked like "
        + thing
        + " .I flew to "
        + place
        + " with my bestfriend and "
        + person
        + " who was a "
        + adjective1
        + " "
        + insect
        + " .We ate some "
        + food
        + " when we got there and then decided to "
        + verb
        + " and the dream ended when I said-- lets "
        + verb
        + "."
    )

def madlib3():
    person = input('enter person name: ')
    color = input('enter color : ')
    foods = input('enter food name : ')
    adjective = input('enter aa adjective name: ')
    thing = input('enter a thing name : ')
    place = input('enter place : ')
    verb = input('enter verb : ')
    adverb = input('enter adverb : ')
    food = input('enter food name: ')
    things = input('enter a thing name : ')

    print(
        "Today we picked apple from "
        + person
        + "'s Orchard. I had no idea there were so many different varieties of apples. I ate "
        + color
        + " apples straight off the tree that tested like "
        + foods
        + ". Then there was a "
        + adjective
        + " apple that looked like a "
        + thing
        + ".When our bag were full, we went on a free hay ride to "
        + place
        + " and back. It ended at a hay pile where we got to "
        + verb
        + " "
        + adverb
        + ". I can hardly wait to get home and cook with the apples. We are going to make appple "
        + food
        + " and "
        + things
        + " pies!."
    )

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MadLibGenerator()
    window.show()

    sys.exit(app.exec_())
