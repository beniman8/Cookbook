
# themes_with_tabs.py
# PyQt5 Theme Collection + Theme Switcher
# Includes matching QTabWidget / QTabBar styling for every theme.

THEMES = {
    "dark_modern": r"""QWidget { background-color: #1e1e2e; color: #ffffff; font-size: 14px; font-family: Segoe UI; }
QMainWindow { background-color: #181825; }
QFrame { background-color: #2a2a3c; border-radius: 10px; }
QPushButton { background-color: #7c3aed; border: none; padding: 10px 18px; border-radius: 8px; font-weight: bold; }
QPushButton:hover { background-color: #8b5cf6; }
QPushButton:pressed { background-color: #6d28d9; }
QLineEdit { background-color: #313244; border: 2px solid #45475a; padding: 8px; border-radius: 6px; }
QLineEdit:focus { border: 2px solid #7c3aed; }
QTabWidget::pane { background-color: #1e1e2e; border: 1px solid #45475a; border-radius: 10px; padding: 6px; }
QTabBar::tab { background-color: #313244; color: #cdd6f4; padding: 10px 18px; margin-right: 4px; border-top-left-radius: 8px; border-top-right-radius: 8px; }
QTabBar::tab:hover { background-color: #45475a; }
QTabBar::tab:selected { background-color: #7c3aed; color: white; font-weight: bold; }
""",

    "glassmorphism": r"""QWidget { background-color: rgba(30,30,46,220); color: white; font-family: Segoe UI; }
QFrame { background-color: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 15px; }
QPushButton { background-color: rgba(124,58,237,180); border-radius: 12px; padding: 12px; }
QPushButton:hover { background-color: rgba(139,92,246,220); }
QLineEdit { background-color: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.16); border-radius: 10px; padding: 8px; color: white; }
QTabWidget::pane { background-color: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.12); border-radius: 14px; padding: 6px; }
QTabBar::tab { background-color: rgba(255,255,255,0.06); color: white; padding: 10px 18px; margin-right: 4px; border-top-left-radius: 12px; border-top-right-radius: 12px; }
QTabBar::tab:hover { background-color: rgba(139,92,246,160); }
QTabBar::tab:selected { background-color: rgba(124,58,237,220); color: white; font-weight: bold; }
""",

    "cyberpunk": r"""QWidget { background-color: #0d1117; color: #00ffff; font-family: Consolas; }
QFrame { background-color: #111827; border: 1px solid #00ffff; border-radius: 6px; }
QPushButton { background-color: #111827; border: 2px solid #00ffff; color: #00ffff; padding: 10px; border-radius: 5px; }
QPushButton:hover { background-color: #00ffff; color: black; }
QLineEdit { background-color: #111827; border: 2px solid #ff00ff; padding: 8px; color: white; }
QTabWidget::pane { background-color: #0d1117; border: 2px solid #00ffff; border-radius: 6px; padding: 6px; }
QTabBar::tab { background-color: #111827; color: #00ffff; border: 1px solid #00ffff; padding: 10px 18px; margin-right: 4px; border-top-left-radius: 5px; border-top-right-radius: 5px; }
QTabBar::tab:hover { background-color: #ff00ff; color: white; }
QTabBar::tab:selected { background-color: #00ffff; color: black; font-weight: bold; }
""",

    "minimal_apple": r"""QWidget { background-color: #f5f5f7; color: #1d1d1f; font-family: Segoe UI; font-size: 14px; }
QFrame { background: white; border-radius: 18px; border: 1px solid #e5e5e5; }
QPushButton { background: #0071e3; color: white; border-radius: 10px; padding: 10px 18px; border: none; }
QPushButton:hover { background: #2488ff; }
QLineEdit { background: white; border: 2px solid #d2d2d7; border-radius: 10px; padding: 8px; }
QTabWidget::pane { background-color: white; border: 1px solid #d2d2d7; border-radius: 14px; padding: 8px; }
QTabBar::tab { background-color: #e8e8ed; color: #1d1d1f; padding: 10px 18px; margin-right: 4px; border-top-left-radius: 10px; border-top-right-radius: 10px; }
QTabBar::tab:hover { background-color: #d2d2d7; }
QTabBar::tab:selected { background-color: #0071e3; color: white; font-weight: bold; }
""",

    "crt_terminal": r"""QWidget { background-color: #050505; color: #00ff66; font-family: Consolas; font-size: 14px; }
QFrame { border: 1px solid #00ff66; border-radius: 6px; }
QPushButton { background-color: #000000; border: 2px solid #00ff66; padding: 10px; }
QPushButton:hover { background-color: #00ff66; color: black; }
QTextEdit { background: black; border: 1px solid #00ff66; }
QTabWidget::pane { background-color: #000000; border: 1px solid #00ff66; border-radius: 4px; padding: 6px; }
QTabBar::tab { background-color: #050505; color: #00ff66; border: 1px solid #00ff66; padding: 9px 16px; margin-right: 3px; }
QTabBar::tab:hover { background-color: #003b18; }
QTabBar::tab:selected { background-color: #00ff66; color: black; font-weight: bold; }
""",

    "vaporwave": r"""QWidget { background-color: #170b2c; color: #f8f8ff; font-family: Segoe UI; }
QFrame { background-color: #22113d; border: 1px solid #ff00ff; border-radius: 20px; }
QPushButton { background-color: #ff00ff; color: white; border-radius: 14px; padding: 12px; }
QPushButton:hover { background-color: #00e5ff; color: #170b2c; }
QLineEdit { background-color: #22113d; border: 2px solid #00e5ff; border-radius: 10px; padding: 8px; color: white; }
QTabWidget::pane { background-color: #22113d; border: 1px solid #ff00ff; border-radius: 16px; padding: 6px; }
QTabBar::tab { background-color: #170b2c; color: #f8f8ff; border: 1px solid #ff00ff; padding: 10px 18px; margin-right: 4px; border-top-left-radius: 12px; border-top-right-radius: 12px; }
QTabBar::tab:hover { background-color: #00e5ff; color: #170b2c; }
QTabBar::tab:selected { background-color: #ff00ff; color: white; font-weight: bold; }
""",

    "industrial_scifi": r"""QWidget { background-color: #101418; color: #d6dde6; font-family: Bahnschrift; }
QFrame { background-color: #161b22; border: 1px solid #2d333b; border-radius: 4px; }
QPushButton { background-color: #1f6feb; border: 1px solid #58a6ff; padding: 10px; border-radius: 4px; }
QPushButton:hover { background-color: #388bfd; }
QLineEdit { background-color: #161b22; border: 1px solid #2d333b; padding: 8px; color: #d6dde6; }
QTabWidget::pane { background-color: #161b22; border: 1px solid #2d333b; border-radius: 4px; padding: 6px; }
QTabBar::tab { background-color: #101418; color: #d6dde6; border: 1px solid #2d333b; padding: 10px 18px; margin-right: 3px; }
QTabBar::tab:hover { background-color: #1f6feb; color: white; }
QTabBar::tab:selected { background-color: #58a6ff; color: #101418; font-weight: bold; }
""",

    "cozy_pixel": r"""QWidget { background-color: #f6ecd9; color: #5c4033; font-family: Verdana; }
QFrame { background-color: #fff8ee; border: 3px solid #d9b382; border-radius: 16px; }
QPushButton { background-color: #86c06c; border: 2px solid #5b8c4a; border-radius: 12px; padding: 10px; color: white; }
QPushButton:hover { background-color: #9ed983; }
QLineEdit { background-color: #fffdf8; border: 2px solid #d9b382; border-radius: 10px; padding: 8px; }
QTabWidget::pane { background-color: #fff8ee; border: 3px solid #d9b382; border-radius: 14px; padding: 8px; }
QTabBar::tab { background-color: #f6ecd9; color: #5c4033; border: 2px solid #d9b382; padding: 10px 18px; margin-right: 4px; border-top-left-radius: 12px; border-top-right-radius: 12px; }
QTabBar::tab:hover { background-color: #f0d6aa; }
QTabBar::tab:selected { background-color: #86c06c; color: white; font-weight: bold; }
""",

    "amoled": r"""QWidget { background-color: #000000; color: #ffffff; font-family: Inter; }
QFrame { background-color: #0b0b0b; border: 1px solid #1f1f1f; border-radius: 16px; }
QPushButton { background-color: #121212; border: 1px solid #2c2c2c; border-radius: 12px; padding: 10px; }
QPushButton:hover { border: 1px solid #8b5cf6; background-color: #181818; }
QLineEdit { background-color: #0f0f0f; border: 2px solid #222; border-radius: 10px; padding: 8px; color: white; }
QTabWidget::pane { background-color: #000000; border: 1px solid #1f1f1f; border-radius: 12px; padding: 6px; }
QTabBar::tab { background-color: #0b0b0b; color: #ffffff; border: 1px solid #1f1f1f; padding: 10px 18px; margin-right: 4px; border-top-left-radius: 10px; border-top-right-radius: 10px; }
QTabBar::tab:hover { border: 1px solid #8b5cf6; background-color: #181818; }
QTabBar::tab:selected { background-color: #8b5cf6; color: white; font-weight: bold; }
""",

    "luxury_gold": r"""QWidget { background-color: #121212; color: #f4e7c5; font-family: Georgia; }
QFrame { background-color: #1e1e1e; border: 1px solid #c8a95b; border-radius: 14px; }
QPushButton { background-color: #c8a95b; color: black; border-radius: 10px; padding: 10px 16px; font-weight: bold; }
QPushButton:hover { background-color: #e6c97f; }
QLineEdit { background-color: #181818; border: 1px solid #c8a95b; border-radius: 10px; padding: 8px; color: #f4e7c5; }
QTabWidget::pane { background-color: #1e1e1e; border: 1px solid #c8a95b; border-radius: 12px; padding: 6px; }
QTabBar::tab { background-color: #121212; color: #f4e7c5; border: 1px solid #c8a95b; padding: 10px 18px; margin-right: 4px; border-top-left-radius: 10px; border-top-right-radius: 10px; }
QTabBar::tab:hover { background-color: #2a2418; }
QTabBar::tab:selected { background-color: #c8a95b; color: black; font-weight: bold; }
""",

    "steam_launcher": r"""QWidget { background-color: #171a21; color: #c7d5e0; font-family: Segoe UI; }
QFrame { background-color: #1b2838; border-radius: 10px; }
QPushButton { background-color: #2a475e; border-radius: 8px; padding: 10px; border: none; }
QPushButton:hover { background-color: #66c0f4; color: black; }
QLineEdit { background-color: #1b2838; border: 1px solid #2a475e; border-radius: 8px; padding: 8px; color: #c7d5e0; }
QTabWidget::pane { background-color: #1b2838; border: 1px solid #2a475e; border-radius: 10px; padding: 6px; }
QTabBar::tab { background-color: #171a21; color: #c7d5e0; padding: 10px 18px; margin-right: 4px; border-top-left-radius: 8px; border-top-right-radius: 8px; }
QTabBar::tab:hover { background-color: #2a475e; }
QTabBar::tab:selected { background-color: #66c0f4; color: black; font-weight: bold; }
""",

    "material_design": r"""QWidget { background-color: #202124; color: #e8eaed; font-family: Roboto; }
QFrame { background-color: #2d2f31; border-radius: 12px; }
QPushButton { background-color: #4285f4; border-radius: 8px; padding: 10px 18px; border: none; color: white; }
QPushButton:hover { background-color: #5a95f5; }
QLineEdit { background-color: #303134; border: 2px solid #5f6368; border-radius: 8px; padding: 8px; color: #e8eaed; }
QLineEdit:focus { border: 2px solid #4285f4; }
QTabWidget::pane { background-color: #2d2f31; border: 1px solid #5f6368; border-radius: 10px; padding: 6px; }
QTabBar::tab { background-color: #303134; color: #e8eaed; padding: 10px 18px; margin-right: 4px; border-top-left-radius: 8px; border-top-right-radius: 8px; }
QTabBar::tab:hover { background-color: #3c4043; }
QTabBar::tab:selected { background-color: #4285f4; color: white; font-weight: bold; }
""",

    "anime_hud": r"""QWidget { background-color: #09111f; color: #7df9ff; font-family: Orbitron; }
QFrame { background-color: rgba(0,20,40,180); border: 1px solid #00e5ff; border-radius: 6px; }
QPushButton { background-color: transparent; border: 2px solid #00e5ff; padding: 10px; border-radius: 4px; }
QPushButton:hover { background-color: #00e5ff; color: black; }
QProgressBar { border: 1px solid #00e5ff; background: transparent; }
QProgressBar::chunk { background-color: #00e5ff; }
QTabWidget::pane { background-color: rgba(0,20,40,180); border: 1px solid #00e5ff; border-radius: 6px; padding: 6px; }
QTabBar::tab { background-color: #09111f; color: #7df9ff; border: 1px solid #00e5ff; padding: 10px 18px; margin-right: 4px; border-top-left-radius: 6px; border-top-right-radius: 6px; }
QTabBar::tab:hover { background-color: #00344a; }
QTabBar::tab:selected { background-color: #00e5ff; color: black; font-weight: bold; }
QTabBar::tab:disabled { color: #2c6b75; border-color: #164d57; }
""",

}


AVAILABLE_THEMES = list(THEMES.keys())


def apply_theme(app, theme_name):
    if theme_name not in THEMES:
        raise ValueError(f"Theme '{theme_name}' not found. Available: {AVAILABLE_THEMES}")
    app.setStyleSheet(THEMES[theme_name])


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import (
        QApplication, QWidget, QVBoxLayout, QPushButton,
        QLineEdit, QLabel, QComboBox, QFrame, QTabWidget
    )

    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(800, 550)

    layout = QVBoxLayout(window)

    title = QLabel("PyQt5 Theme Showcase with QTabWidget")
    combo = QComboBox()
    combo.addItems(AVAILABLE_THEMES)

    input_box = QLineEdit()
    input_box.setPlaceholderText("Type here...")

    button = QPushButton("Sample Button")

    tabs = QTabWidget()

    tab1 = QWidget()
    tab1_layout = QVBoxLayout(tab1)
    tab1_layout.addWidget(QLabel("Dashboard Tab"))
    tab1_layout.addWidget(QPushButton("Dashboard Button"))

    tab2 = QWidget()
    tab2_layout = QVBoxLayout(tab2)
    tab2_layout.addWidget(QLabel("Settings Tab"))
    tab2_layout.addWidget(QLineEdit("Settings input"))

    tabs.addTab(tab1, "Dashboard")
    tabs.addTab(tab2, "Settings")

    card = QFrame()
    card.setMinimumHeight(100)

    layout.addWidget(title)
    layout.addWidget(combo)
    layout.addWidget(input_box)
    layout.addWidget(button)
    layout.addWidget(tabs)
    layout.addWidget(card)

    def change_theme():
        apply_theme(app, combo.currentText())

    combo.currentTextChanged.connect(change_theme)

    apply_theme(app, "dark_modern")

    window.show()
    sys.exit(app.exec_())
