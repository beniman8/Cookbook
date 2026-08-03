
# themes.py
# PyQt5 Theme Collection + Theme Switcher
# ----------------------------------------

THEMES = {

    "dark_modern": """
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

    QLineEdit {
        background-color: #313244;
        border: 2px solid #45475a;
        padding: 8px;
        border-radius: 6px;
    }

    QFrame {
        background-color: #2a2a3c;
        border-radius: 10px;
    }
    """,


    "glassmorphism": """
    QWidget {
        background-color: rgba(30,30,46,220);
        color: white;
        font-family: Segoe UI;
    }

    QFrame {
        background-color: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 15px;
    }

    QPushButton {
        background-color: rgba(124,58,237,180);
        border-radius: 12px;
        padding: 12px;
    }

    QPushButton:hover {
        background-color: rgba(139,92,246,220);
    }
    """,


    "cyberpunk": """
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
    """,


    "minimal_apple": """
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
    """,


    "crt_terminal": """
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
    """,


    "vaporwave": """
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
    """,


    "industrial_scifi": """
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
    """,


    "cozy_pixel": """
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
    """,


    "amoled": """
    QWidget {
        background-color: #000000;
        color: #ffffff;
        font-family: Inter;
    }

    QFrame {
        background-color: #0b0b0b;
        border: 1px solid #1f1f1f;
        border-radius: 16px;
    }

    QPushButton {
        background-color: #121212;
        border: 1px solid #2c2c2c;
        border-radius: 12px;
        padding: 10px;
    }

    QPushButton:hover {
        border: 1px solid #8b5cf6;
        background-color: #181818;
    }
    """,


    "luxury_gold": """
    QWidget {
        background-color: #121212;
        color: #f4e7c5;
        font-family: Georgia;
    }

    QFrame {
        background-color: #1e1e1e;
        border: 1px solid #c8a95b;
        border-radius: 14px;
    }

    QPushButton {
        background-color: #c8a95b;
        color: black;
        border-radius: 10px;
        padding: 10px 16px;
        font-weight: bold;
    }

    QPushButton:hover {
        background-color: #e6c97f;
    }
    """,


    "steam_launcher": """
    QWidget {
        background-color: #171a21;
        color: #c7d5e0;
        font-family: Segoe UI;
    }

    QFrame {
        background-color: #1b2838;
        border-radius: 10px;
    }

    QPushButton {
        background-color: #2a475e;
        border-radius: 8px;
        padding: 10px;
        border: none;
    }

    QPushButton:hover {
        background-color: #66c0f4;
        color: black;
    }
    """,


    "material_design": """
    QWidget {
        background-color: #202124;
        color: #e8eaed;
        font-family: Roboto;
    }

    QFrame {
        background-color: #2d2f31;
        border-radius: 12px;
    }

    QPushButton {
        background-color: #4285f4;
        border-radius: 8px;
        padding: 10px 18px;
        border: none;
        color: white;
    }

    QPushButton:hover {
        background-color: #5a95f5;
    }
    """,


    "anime_hud": """
    QWidget {
        background-color: #09111f;
        color: #7df9ff;
        font-family: Orbitron;
    }

    QFrame {
        background-color: rgba(0,20,40,180);
        border: 1px solid #00e5ff;
        border-radius: 6px;
    }

    QPushButton {
        background-color: transparent;
        border: 2px solid #00e5ff;
        padding: 10px;
        border-radius: 4px;
    }

    QPushButton:hover {
        background-color: #00e5ff;
        color: black;
    }
    """
}



# ----------------------------------------
# THEME HELPER FUNCTIONS
# ----------------------------------------

def apply_theme(app, theme_name):
    if theme_name in THEMES:
        app.setStyleSheet(THEMES[theme_name])
    else:
        print(f"Theme '{theme_name}' not found.")



# ----------------------------------------
# AVAILABLE THEMES
# ----------------------------------------

AVAILABLE_THEMES = list(THEMES.keys())



# ----------------------------------------
# EXAMPLE USAGE
# ----------------------------------------

if __name__ == "__main__":

    import sys

    from PyQt5.QtWidgets import (
        QApplication,
        QWidget,
        QVBoxLayout,
        QPushButton,
        QLineEdit,
        QLabel,
        QComboBox,
        QFrame
    )

    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(700, 500)

    layout = QVBoxLayout()

    title = QLabel("PyQt5 Theme Showcase")

    combo = QComboBox()
    combo.addItems(AVAILABLE_THEMES)

    input_box = QLineEdit()
    input_box.setPlaceholderText("Type here...")

    button = QPushButton("Sample Button")

    card = QFrame()
    card.setMinimumHeight(150)

    layout.addWidget(title)
    layout.addWidget(combo)
    layout.addWidget(input_box)
    layout.addWidget(button)
    layout.addWidget(card)

    window.setLayout(layout)

    def change_theme():
        theme = combo.currentText()
        apply_theme(app, theme)

    combo.currentTextChanged.connect(change_theme)

    apply_theme(app, "dark_modern")

    window.show()

    sys.exit(app.exec_())
