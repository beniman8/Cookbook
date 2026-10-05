

import sys  
#Ignore the deprecation warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

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
    
    
)


class APP(QWidget):
    
    def __init__(self):
        super().__init__()

        
        
        self.initUI()
        
        
    def initUI(self):
            
        self.setWindowTitle("ALARM CLOCK")
        self.setGeometry(500,100,800,800)
        
        
        
        self.main_layout = QVBoxLayout()
        
        
        self.image_display = QLabel("HELLO WORLD")
        
        self.main_layout.addWidget(self.image_display)
        
        self.setLayout(self.main_layout)
        
        self.setStyleSheet(cozy_style)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    application = APP()
    
    
    application.show()
    
    sys.exit(app.exec_())





