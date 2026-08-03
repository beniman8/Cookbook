# (weight / height ) **2 BMI calculation
#TODO toggle switch from imperial to metric
import sys 



from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QComboBox,
)





class BMICalculator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.unit_var = "METRIC"
        
        
        self.initUI()
        
        
    def initUI(self):
        
        self.setWindowTitle("BMI CALCULATOR")
        
        main_layout = QVBoxLayout()
        
        
        #display 
        self.display = QLabel("BMI CALCULATOR")
        
        #button
        self.button = QPushButton("Calculate My BMI")
        
        # Input fields 
        self.heightt = QLineEdit()
        self.heightt.setMaxLength(3)
        self.heightt.setPlaceholderText("Enter your height inches or centimeters")
        
        self.weight = QLineEdit()
        self.weight.setMaxLength(3)
        self.weight.setPlaceholderText("Enter your weight in pounds or kilograms")
        
        #combobox
        
        units= QComboBox()
        units.addItems(["METRIC","IMPERIAL"])
        units.currentTextChanged.connect(self.change_unit)
        
        
        self.button.clicked.connect(self.calculate_bmi)
        
        main_layout.addWidget(self.heightt)
        main_layout.addWidget(self.weight)
        main_layout.addWidget(units)
        main_layout.addWidget(self.display)
        main_layout.addWidget(self.button)
        
        
        self.setLayout(main_layout)
        
        
        self.setStyleSheet(
            
        """
            QPushButton,QLabel,QLineEdit{
                padding:20px;
                
                font-weight: bold;
                
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
            QLineEdit{
                font-size:25px;
            }
        
        """
        )
        
        
    def calculate_bmi(self):
        height = int(self.heightt.text())
        weight = int(self.weight.text())



        if self.unit_var == "METRIC":
            # kilograms and centimeters
            
            res = weight / height ** 2
            self.display.setText(str(res))
            
            
            
            
        elif self.unit_var == "IMPERIAL":
            # pounds and inches 
            res = (weight * 703) / height **2
            self.display.setText(str(res))
            
            
            
            
    def change_unit(self,unit):
        self.unit_var = unit
        
        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    bmi_calculator = BMICalculator()
    
    
    bmi_calculator.show()
    
    sys.exit(app.exec_())
