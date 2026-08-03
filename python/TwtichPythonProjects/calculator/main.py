import sys
import ast
import operator

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


# Safe math operators
operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}


def safe_eval(expr):
    """Safely evaluate math expressions"""

    def eval_node(node):
        if isinstance(node, ast.Constant):
            return node.value

        if isinstance(node, ast.BinOp):
            return operators[type(node.op)](
                eval_node(node.left),
                eval_node(node.right)
            )

    tree = ast.parse(expr, mode='eval')
    return eval_node(tree.body)


class Calculator(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Modern Calculator")
        self.setGeometry(700, 300, 350, 450)

        self.expression = ""

        self.initUI()

    def initUI(self):

        main_layout = QVBoxLayout()

        # Display
        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet("""
            font-size: 40px;
            padding: 20px;
            background: #1e1e1e;
            color: white;
            border-radius: 10px;
        """)

        main_layout.addWidget(self.display)

        grid = QGridLayout()

        buttons = [

            ('7',0,0), ('8',0,1), ('9',0,2), ('/',0,3),
            ('4',1,0), ('5',1,1), ('6',1,2), ('*',1,3),
            ('1',2,0), ('2',2,1), ('3',2,2), ('-',2,3),
            ('0',3,0), ('C',3,1), ('=',3,2), ('+',3,3)

        ]

        for text, row, col in buttons:

            button = QPushButton(text)

            button.setFixedSize(70,60)

            button.setStyleSheet("""
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

            button.clicked.connect(lambda _, t=text: self.on_button(t))
    

            grid.addWidget(button,row,col)

        main_layout.addLayout(grid)

        widget = QWidget()
        widget.setLayout(main_layout)

        self.setCentralWidget(widget)

        # Dark window theme
        self.setStyleSheet("background:#121212;")

    def on_button(self, char):

        if char == "C":
            self.expression = ""
            self.display.setText("0")
            return

        if char == "=":

            try:
                result = safe_eval(self.expression)
                self.display.setText(str(result))
                self.expression = str(result)

            except:
                self.display.setText("Error")
                self.expression = ""

            return

        self.expression += char
        self.display.setText(self.expression)

    # Keyboard support
    def keyPressEvent(self, event):

        key = event.text()

        allowed = "0123456789+-*/"

        if key in allowed:
            self.on_button(key)

        if event.key() == Qt.Key_Return:
            self.on_button("=")

        if event.key() == Qt.Key_Backspace:
            self.expression = self.expression[:-1]
            self.display.setText(self.expression if self.expression else "0")


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec_())