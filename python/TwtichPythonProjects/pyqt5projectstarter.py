import os 

dir_path = os.path.dirname(os.path.realpath(__file__))



main_content = """

import sys  

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
            
        self.setWindowTitle("APP NAME")
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





"""


with open(f"{dir_path}\main.py", "w", encoding="utf-8") as f:
    f.write(main_content)

print("file created: main.py")


style_sheet = '''


"""
This is a folder where i store stylesheets for all my program

"""


original_style = """
        QPushButton,QLabel{
            padding:20px;
            
            font-weight:bold;
            font-family:calibri;
        }
        
        QPushButton{
            font-size:50px;
        }
        QLabel{
            font-size:120px;
            
            
            border-radius:20px;
        }
        QComboBox{
            font-size:50px;
        }
        
        """
        
dark_style = """
QWidget {
    background-color: #1e1e2e;
    color: #ffffff;
    font-size: 14px;
    font-family: Segoe UI;
}

QMainWindow {
    background-color: #181825;
}

QPushButton {
    background-color: #7c3aed;
    border: none;
    padding: 10px 18px;
    border-radius: 8px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #8b5cf6;
}

QPushButton:pressed {
    background-color: #6d28d9;
}

QLineEdit {
    background-color: #313244;
    border: 2px solid #45475a;
    padding: 8px;
    border-radius: 6px;
}

QLineEdit:focus {
    border: 2px solid #7c3aed;
}

QListWidget {
    background-color: #313244;
    border-radius: 8px;
    padding: 5px;
}

QListWidget::item:selected {
    background-color: #7c3aed;
    border-radius: 4px;
}

QComboBox {
    background-color: #313244;
    border-radius: 6px;
    padding: 6px;
}

QScrollBar:vertical {
    border: none;
    background: #1e1e2e;
    width: 10px;
}

QScrollBar::handle:vertical {
    background: #7c3aed;
    border-radius: 5px;
}
"""+ original_style


glass_style = """
QWidget {
    background-color: rgba(30, 30, 46, 220);
    color: white;
    font-family: Segoe UI;
}

QFrame {
    background-color: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 15px;
}

QPushButton {
    background-color: rgba(124, 58, 237, 180);
    border-radius: 12px;
    padding: 12px;
    border: 1px solid rgba(255,255,255,0.1);
}

QPushButton:hover {
    background-color: rgba(139, 92, 246, 220);
}
"""+ original_style


cyberpunk_style = """
QWidget {
    background-color: #0d1117;
    color: #00ffff;
    font-family: Consolas;
}

QPushButton {
    background-color: #111827;
    border: 2px solid #00ffff;
    color: #00ffff;
    padding: 10px;
    border-radius: 5px;
}

QPushButton:hover {
    background-color: #00ffff;
    color: black;
}

QLineEdit {
    background-color: #111827;
    border: 2px solid #ff00ff;
    padding: 8px;
    color: white;
}
"""+ original_style


minimal_style = """
QWidget {
    background-color: #f5f5f7;
    color: #1d1d1f;
    font-family: Segoe UI;
    font-size: 14px;
}

QFrame {
    background: white;
    border-radius: 18px;
    border: 1px solid #e5e5e5;
}

QPushButton {
    background: #0071e3;
    color: white;
    border-radius: 10px;
    padding: 10px 18px;
    border: none;
}

QPushButton:hover {
    background: #2488ff;
}

QLineEdit {
    background: white;
    border: 2px solid #d2d2d7;
    border-radius: 10px;
    padding: 8px;
}

"""+ original_style

retro_style = """
QWidget {
    background-color: #050505;
    color: #00ff66;
    font-family: Consolas;
    font-size: 14px;
}

QFrame {
    border: 1px solid #00ff66;
    border-radius: 6px;
}

QPushButton {
    background-color: #000000;
    border: 2px solid #00ff66;
    padding: 10px;
}

QPushButton:hover {
    background-color: #00ff66;
    color: black;
}

QTextEdit {
    background: black;
    border: 1px solid #00ff66;
}


"""+ original_style


neon_style = """

QWidget {
    background-color: #170b2c;
    color: #f8f8ff;
    font-family: Segoe UI;
}

QFrame {
    background-color: #22113d;
    border: 1px solid #ff00ff;
    border-radius: 20px;
}

QPushButton {
    background-color: #ff00ff;
    color: white;
    border-radius: 14px;
    padding: 12px;
}

QPushButton:hover {
    background-color: #00e5ff;
}

QLineEdit {
    background-color: #22113d;
    border: 2px solid #00e5ff;
    border-radius: 10px;
    padding: 8px;
}
"""+ original_style


scifi_style = """
QWidget {
    background-color: #101418;
    color: #d6dde6;
    font-family: Bahnschrift;
}

QFrame {
    background-color: #161b22;
    border: 1px solid #2d333b;
    border-radius: 4px;
}

QPushButton {
    background-color: #1f6feb;
    border: 1px solid #58a6ff;
    padding: 10px;
    border-radius: 4px;
}

QPushButton:hover {
    background-color: #388bfd;
}

QProgressBar::chunk {
    background-color: #00c853;
}

"""+ original_style

cozy_style = """
QWidget {
    background-color: #f6ecd9;
    color: #5c4033;
    font-family: Verdana;
}

QFrame {
    background-color: #fff8ee;
    border: 3px solid #d9b382;
    border-radius: 16px;
}

QPushButton {
    background-color: #86c06c;
    border: 2px solid #5b8c4a;
    border-radius: 12px;
    padding: 10px;
    color: white;
}

QPushButton:hover {
    background-color: #9ed983;
}

QLineEdit {
    background-color: #fffdf8;
    border: 2px solid #d9b382;
    border-radius: 10px;
    padding: 8px;
}

"""+ original_style





'''

with open(f"{dir_path}\stylesheet.py", "w", encoding="utf-8") as f:
    f.write(style_sheet)

print("file created: stylesheet.py")

os.remove(__file__)
print("The current file has been successfully deleted.")