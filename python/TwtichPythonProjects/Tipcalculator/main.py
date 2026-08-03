import sys 



from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QLineEdit
    
)


class TipCalculator(QWidget):
    
    
    
    def __init__(self):
        super().__init__()
        
        
        
        self.initUI()
        
        
    def initUI(self):
        
        self.setWindowTitle("TIP CALCULATOR")
        
        main_layout = QVBoxLayout()
        
        #display
        self.display_label = QLabel("Your TIP",self)
        
        #input
        self.bill_amount = QLineEdit(self)
        
        #button
        self.button_15 = QPushButton("15%",self)
        
        self.button_20 = QPushButton("20%",self)
        
        self.button_30 = QPushButton("30%",self)
        
        main_layout.addWidget(self.display_label)
        main_layout.addWidget(self.bill_amount)
        main_layout.addWidget(self.button_15)
        main_layout.addWidget(self.button_20)
        main_layout.addWidget(self.button_30)
        
        
        self.setLayout(main_layout)
        
        self.button_15.clicked.connect(lambda _, p="15": self.calculate_tip(p))
        self.button_20.clicked.connect(lambda _, p="20":self.calculate_tip(p))
        self.button_30.clicked.connect(lambda _, p="30":self.calculate_tip(p))
        
        self.setStyleSheet(
            
        """
        QPushButton, QLabel{
            padding: 20px;
            font-weight: bold;
            font-family:calibri;
            
        }
        QPushButton{
            font-size: 50px;
        }
        QLabel{
            font-size:120px;
            
            background-color:blue;
            
            border-radius: 20px;
        }
        
        
        """
        )
        
        
    def calculate_tip(self,percentage):
        bill = int(self.bill_amount.text())
        calculate_percentage = bill * (int(percentage) / 100)
        self.display_label.setText(f"you owe : {calculate_percentage + bill}")
    
        
        
        
        
if __name__ == "__main__":
    app  = QApplication(sys.argv)
    
    tip_calculator = TipCalculator()
    
    tip_calculator.show()
    
    sys.exit(app.exec_())
    