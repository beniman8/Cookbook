import sys 


from PyQt5.QtWidgets import(
    
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QInputDialog,
)

from PyQt5.QtCore import QTimer , QTime, Qt 


class CountDownTimer(QWidget):
    
    
    def __init__(self):
        super().__init__()
        
        self.total_seconds = 0
                

  
    

        
        self.initUI()
        

        


    def initUI(self):
        
        self.setWindowTitle("COUNTDOWN TIMER")
        
        main_layout = QVBoxLayout()
        
        #DISPLAY
        self.time_label = QLabel("00:00",self)
        
        #TIME INPUT
        self.timer_input = QInputDialog()
        
        
        #SET TIMER 
        self.set_timer = QPushButton("Set time",self)
        self.set_timer.clicked.connect(self.set_time)
        
        
        #START COUNTDOWN TIMER
        self.countdown_button = QPushButton("START THE COUNTDOWN",self)
        self.countdown_button.clicked.connect(self.start_timer)
        
        main_layout.addWidget(self.time_label)
        main_layout.addWidget(self.set_timer)
        main_layout.addWidget(self.countdown_button)
        
        
        self.setLayout(main_layout)
        self.timer = QTimer(self)
        
        self.setStyleSheet(""" 
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
                        
                        border-radius:20px;
                    }
                    
                    
                    """)
        
        
        #connecting our timer so it can update the display 
        self.timer.timeout.connect(self.update_display)
        
        
        
        
        
    def set_time(self):
        seconds , ok = self.timer_input.getInt(self,"Timer","Enter Seconds:")
        
        if ok:
            self.total_seconds = seconds
            self.time_label.setText(f"{self.total_seconds // 60:02d}:{self.total_seconds % 60:02d}")
            
            
    def start_timer(self):
        
        if self.total_seconds > 0:
            self.timer.start(1000)#tick the clock every 1 second
            
            
        
    
    def update_display(self):
        if self.total_seconds >0:
            self.total_seconds -= 1
            mins,secs =divmod(self.total_seconds,60)
            self.time_label.setText(f"{mins:02d} : {secs:02d}")
            
        else:
            self.timer.stop()
            self.time_label.setText("finish")



if __name__ == "__main__":
    app=QApplication(sys.argv)
    
    cd_timer = CountDownTimer()
    
    cd_timer.show()
    
    sys.exit(app.exec_())