import sys 




from PyQt5.QtWidgets import(
    QMainWindow,
    QApplication,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QLineEdit,

)


SCREEN_WIDTH,SCREEN_HEIGHT = 700 , 700


class MadLibGenerator(QMainWindow):
    
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MADLIBS GENERATOR")
        self.setGeometry(700,300,SCREEN_WIDTH,SCREEN_HEIGHT)
        
        
        
        self.initUI()
        
    def initUI(self):
        
        #OUR MAIN LAYOUT
        main_layout = QVBoxLayout()
        
        #BUTTON
        self.button1 = QPushButton("First MadLibs")
        #BUTTON FUNCTIONALITY 
        self.button1.clicked.connect(self.madlib1)
        
        
        #INPUTS 
        self.animals= QLineEdit(self)
        self.profession = QLineEdit(self)
        self.cloth = QLineEdit(self)
        self.things =QLineEdit(self)
        self.name= QLineEdit(self)
        self.place = QLineEdit(self)
        self.verb = QLineEdit(self)
        self.food = QLineEdit(self)


        self.animals.setPlaceholderText('animals')
        self.profession.setPlaceholderText('profession')
        self.cloth.setPlaceholderText('cloth')
        self.things.setPlaceholderText('things')
        self.name.setPlaceholderText('name')
        self.place.setPlaceholderText('place')
        self.verb.setPlaceholderText('verb')
        self.food.setPlaceholderText('food')        
        
        
        
        #BUTTON PLACEMENT
        main_layout.addWidget(self.button1)
        
        #ADD INPUTS TO SCREEN
        main_layout.addWidget(self.animals)
        main_layout.addWidget(self.profession)
        main_layout.addWidget(self.cloth)
        main_layout.addWidget(self.things)
        main_layout.addWidget(self.name)
        main_layout.addWidget(self.place)
        main_layout.addWidget(self.verb)
        main_layout.addWidget(self.food)

        
        
        widget = QWidget()
        widget.setLayout(main_layout)
        
        self.setCentralWidget(widget)
        

        
    def madlib1(self):
        

        print(
            "say "
            + self.food.text()
            + ", the photographer said as the camera flashed! "
            + self.name.text()
            + " and I had gone to "
            + self.place.text()
            + " to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as "
            + self.animals.text()
            + " pretending to be a "
            + self.profession.text()
            + ". when we saw the second photo, it was exactly what I wanted. We both looked like "
            + self.things.text()
            + " wearing "
            + self.cloth.text()
            + " and "
            + self.verb.text()
            + " --exactly what I had in mind"
        )

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    window = MadLibGenerator()
    window.show()
    
    
    sys.exit(app.exec_())