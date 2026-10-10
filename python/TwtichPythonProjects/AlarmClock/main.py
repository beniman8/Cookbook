
#Ignore the deprecation warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import sys  
import winsound


from PyQt5.QtCore import QTime,QTimer,Qt

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
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QTimeEdit
    
    
)


class APP(QWidget):
    
    def __init__(self):
        super().__init__()

        
        self.alarms = {}

        self.initUI()
        
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

        self.timer.start(1000)
        
        
        
    def initUI(self):
        

        self.setWindowTitle("ALARM CLOCK")
        self.setGeometry(500,100,800,400)
        
        self.bt_1 = QPushButton('SET ALARM 1')
        self.al_1 = QTimeEdit()
        self.al_1.setDisplayFormat("hh:mm:ss AP")
        
        
        self.bt_2 = QPushButton('SET ALARM 2')
        self.al_2 = QTimeEdit()
        self.al_2.setDisplayFormat("hh:mm:ss AP")
        
        
        self.bt_3 = QPushButton('SET ALARM 3')
        self.al_3 = QTimeEdit()
        self.al_3.setDisplayFormat("hh:mm:ss AP")
        
        
        self.bt_4 = QPushButton('SET ALARM 4')
        self.al_4 = QTimeEdit()
        self.al_4.setDisplayFormat("hh:mm:ss AP")        
        
        
        
        self.main_layout = QHBoxLayout()
        
        self.button_layout = QVBoxLayout()
        self.button_layout.addWidget(self.bt_1)
        self.button_layout.addWidget(self.al_1)
        
        self.button_layout.addWidget(self.bt_2)
        self.button_layout.addWidget(self.al_2)
        
        
        self.button_layout.addWidget(self.bt_3)
        self.button_layout.addWidget(self.al_3)
        
        
        self.button_layout.addWidget(self.bt_4)
        self.button_layout.addWidget(self.al_4)
        
        
        self.image_display = QLabel("ALARM CLOCK")
        
        
        self.main_layout.addLayout(self.button_layout)
        
        self.main_layout.addWidget(self.image_display)
        
        self.setLayout(self.main_layout)
        
        self.setStyleSheet(dark_style)
        
        
        self.bt_1.clicked.connect(lambda _:self.set_alarm(1,self.al_1))
        self.bt_2.clicked.connect(lambda _:self.set_alarm(2,self.al_2))
        self.bt_3.clicked.connect(lambda _:self.set_alarm(3,self.al_3))
        self.bt_4.clicked.connect(lambda _:self.set_alarm(4,self.al_4))
        
        
        
        
    def update_time(self):
        
        self.current_time = QTime.currentTime().toString('hh:mm:ss AP')
        
        self.image_display.setText(f"{self.current_time}")
        
        self.check_alarm()
        
        
        
    def set_alarm(self,alarm_id,alarm):
        
        alarm_time = alarm.time()
    
        self.alarms[alarm_id] = alarm_time
        
        
    def check_alarm(self):
        
        current_time = QTime.currentTime()
        
        for alarm_id , alarm_time in list(self.alarms.items()):
            
            if current_time.hour() == alarm_time.hour() and current_time.minute() == alarm_time.minute():
                print(f"Alarm  {alarm_id} is ringing") 
                winsound.Beep(1000, 1500)
        








if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    application = APP()
    
    
    application.show()
    
    sys.exit(app.exec_())





