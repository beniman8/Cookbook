import stylesheet
from PyQt5.QtGui import QFont, QDoubleValidator
import sys  

from PyQt5 import QtWidgets


#Ignore the deprecation warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from data import get_available_currencies,update_data_from_api,get_value_of_currency
from helper import change_base_rate

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
    
    
)



class CURRENCY_CONVERTER(QWidget):

    def __init__(self):
        super().__init__()
        self.currency_list=get_available_currencies()
        self.initUI()


    def initUI(self):
        
        self.setWindowTitle("CURRENCY CONVERTER")
        self.setGeometry(500,100,800,800)
        self.setStyleSheet(minimal_style)
        main_layout = QVBoxLayout()
        
        combo_layout = QHBoxLayout()
        currency_l= QComboBox()
        currency_r=QComboBox()
        currency_l.addItems(self.currency_list)
        currency_r.addItems(self.currency_list)
        
        currency_l.setEditable(True)
        currency_l.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        currency_l.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        
        currency_r.setEditable(True)
        currency_r.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        currency_r.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        
        value_layout = QHBoxLayout()
        #only allow 
        float_validator = QDoubleValidator(0.0,100000.0,2)
        float_validator.setNotation(QDoubleValidator.StandardNotation)
        value_left=QLineEdit()
        self.value_right= QLabel()
        self.value_right.setFixedSize(400, 60)
        value_left.setValidator(float_validator)
        
        
        
        button_layout = QHBoxLayout()
        convert_bt = QPushButton("CONVERT")
        update_data = QPushButton("UPDATE DATA")
        
        
        
        
        
        #ADDING BUTTON AND STUFF TO GUI
        combo_layout.addWidget(currency_l)
        combo_layout.addWidget(currency_r)
        value_layout.addWidget(value_left,stretch=1)
        value_layout.addWidget(self.value_right,stretch=1)
        button_layout.addWidget(convert_bt)
        button_layout.addWidget(update_data)
        
        main_layout.addLayout(combo_layout)
        main_layout.addLayout(value_layout)
        main_layout.addLayout(button_layout)
        
        
        self.setLayout(main_layout)
        
        
        update_data.clicked.connect(self.update_now)

        convert_bt.clicked.connect(lambda *args :self.convert(currency_l.currentText(),value_left.text(),currency_r.currentText()))
        
        
        
    def update_now(self):
        update_data_from_api()
        
    def convert(self,base,current_cash,new_currency):
        
        value_of_new_currency = get_value_of_currency(new_currency)
        
        if base !='USD':
            self.value_right.setText(str(change_base_rate(get_value_of_currency(base),get_value_of_currency(new_currency)) * float(current_cash)))
        else:
            
            self.value_right.setText(str(float(current_cash) * float(value_of_new_currency)))
            
        
        
        
        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    currency = CURRENCY_CONVERTER()
    
    
    currency.show()
    
    sys.exit(app.exec_())
