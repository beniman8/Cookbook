'''
This is our calculator
TODO make it pretty 
TODO UI ANIMATION
TODO PROGRAM the backspace button
TODO IF you press the equal sign after the operation has been evaluated  . just grab the bottom value and the number after the operator to evaluate it again
TODO if equal has already been pressed and you press an operator . grab the value on the bottom text area and add the operator to it and place it on the top text area
'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout,QLabel,QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(700, 300, 500, 500)
        
        #Buttons 
        self.button0 = QPushButton("0", self)
        self.button1 = QPushButton("1", self)
        self.button2 = QPushButton("2", self)
        self.button3 = QPushButton("3", self) 
        self.button4 = QPushButton("4", self) 
        self.button5 = QPushButton("5", self) 
        self.button6 = QPushButton("6", self) 
        self.button7= QPushButton("7", self) 
        self.button8 = QPushButton("8", self) 
        self.button9 = QPushButton("9", self) 
        self.button_mul = QPushButton("*", self) 
        self.button_div = QPushButton("/", self) 
        self.button_sub = QPushButton("-", self)
        self.button_add = QPushButton("+", self)
        self.button_backspace = QPushButton("<", self)
        self.button_equal = QPushButton("=", self)
        
        
        
        self.top_text_area = QLabel(self)
        self.bottom_text_area = QLabel(self)
        
        
        self.top_area_str =''
        self.bot_area_str =''
        
        
        
        self.initUI()

    def initUI(self):
        
        main_layout = QVBoxLayout()
        
        #Layout setup
        layout = QGridLayout()

        main_layout.addWidget(self.top_text_area)
        main_layout.addWidget(self.bottom_text_area)
        


        #Placement of the buttons
        layout.addWidget(self.button0, 5, 1)
        layout.addWidget(self.button_div, 0, 2)
        
        layout.addWidget(self.button1, 4, 0)
        layout.addWidget(self.button2, 4, 1)
        layout.addWidget(self.button3, 4, 2)
        layout.addWidget(self.button_add,4, 3)
        
        
        layout.addWidget(self.button4, 2, 0)
        layout.addWidget(self.button5, 2, 1)
        layout.addWidget(self.button6, 2, 2)
        layout.addWidget(self.button_sub, 2, 3)        

        
        layout.addWidget(self.button7, 1, 0)
        layout.addWidget(self.button8, 1, 1)
        layout.addWidget(self.button9, 1, 2)
        layout.addWidget(self.button_mul, 1, 3)        
        
        
        layout.addWidget(self.button_backspace,0,3)
        layout.addWidget(self.button_equal,5,3)
        
        #Style the display
        self.top_text_area.setStyleSheet("font-size: 20px;")
        self.bottom_text_area.setStyleSheet("font-size: 30px; font-weight: bold;")

        
        main_layout.addLayout(layout)
        #Main widget area
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        #connect buttons to functions
        self.button0.clicked.connect(lambda: self.append_bot("0"))
        self.button1.clicked.connect(lambda: self.append_bot("1"))
        self.button2.clicked.connect(lambda: self.append_bot("2"))
        self.button3.clicked.connect(lambda: self.append_bot("3"))
        self.button4.clicked.connect(lambda: self.append_bot("4"))
        self.button5.clicked.connect(lambda: self.append_bot("5"))
        self.button6.clicked.connect(lambda: self.append_bot("6"))
        self.button7.clicked.connect(lambda: self.append_bot("7"))
        self.button8.clicked.connect(lambda: self.append_bot("8"))
        self.button9.clicked.connect(lambda: self.append_bot("9"))

        #operators
        self.button_add.clicked.connect(lambda: self.pressed_operator("+"))
        self.button_sub.clicked.connect(lambda: self.pressed_operator("-"))
        self.button_div.clicked.connect(lambda: self.pressed_operator("/"))
        self.button_mul.clicked.connect(lambda: self.pressed_operator("*"))
        

        
        #equal
        self.button_equal.clicked.connect(self.equals)
        
        
        
        


    def on_click(self):
        print("Button clicked!")
        
    def append_bot(self,num):
        '''This method appends the button string value into the top text area'''
        ... 
        self.bot_area_str += num
    
        self.bottom_text_area.setText(self.bot_area_str)
        
        
    def pressed_operator(self,operator):
        '''this fils up the top text area when an operator is pressed'''
        # temp_area = self.bot_area_str
        
        # temp_area += operator
        
        # self.top_area_str = temp_area
        
        # self.top_text_area.setText(self.top_area_str)
        
        # self.bot_area_str =""
        # self.bottom_text_area.setText("")
        if self.bot_area_str == "":
            return
            
        self.top_area_str = self.bot_area_str + operator
        self.top_text_area.setText(self.top_area_str)

        self.bot_area_str = ""
        self.bottom_text_area.setText("")        
        
        
    def backspace(self):
        self.bot_area_str = self.bot_area_str[:-1]
        self.bottom_text_area.setText(self.bot_area_str)
        
    def equals(self):
        
        
        # temp = self.top_area_str
        
        # temp += self.bot_area_str
        
        # res = eval(temp)
        
        # self.bottom_text_area.setText(str(res))
        temp = self.top_area_str + self.bot_area_str

        try:
            res = eval(temp)
            self.bot_area_str = str(res)
            self.bottom_text_area.setText(self.bot_area_str)
            self.top_area_str = ""
            self.top_text_area.setText("")
        except:
            self.bottom_text_area.setText("Error")
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
    
