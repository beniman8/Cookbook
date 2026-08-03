import sys  
import json 
from pathlib import Path 
from datetime import datetime

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
    QTabWidget
    
    
)


class FLASHCARD(QWidget):

    def __init__(self):
        super().__init__()
        
        self.date_studied = None 
        self.date_modified = None
        #TODO
        
        '''
        from datetime import datetime

        # Define two timestamps
        time_str1 = "2026-07-25 08:00:00"
        time_str2 = "2026-07-29 14:30:15"

        # Convert strings to datetime objects
        t1 = datetime.strptime(time_str1, "%Y-%m-%d %H:%M:%S")
        t2 = datetime.strptime(time_str2, "%Y-%m-%d %H:%M:%S")

        # Subtract to get the difference
        difference = t2 - t1

        # Extract specific metrics
        print(f"Days: {difference.days}")                  # Output: 4
        print(f"Total Seconds: {difference.total_seconds()}") # Output: 369015.0
        
        '''
        0


        self.getCards()
        
        

        self.initUI()
        
        
    def getCards(self):
        #Get all the cards that are available or create default cards
        starting_file = {
            "subjects": [
                {
                    "name": "Math",
                    "questions": [
                        {"question": "What is 7 × 8?", "answer": "56"},
                        {"question": "What is the square root of 81?", "answer": "9"},
                        {"question": "What is 15 + 27?", "answer": "42"},
                    ],
                },
                {
                    "name": "Science",
                    "questions": [
                        {
                            "question": "What planet is known as the Red Planet?",
                            "answer": "Mars",
                        },
                        {
                            "question": "What gas do plants absorb from the atmosphere?",
                            "answer": "Carbon dioxide",
                        },
                        {
                            "question": "What is the chemical symbol for water?",
                            "answer": "H2O",
                        },
                    ],
                },
                {
                    "name": "Art",
                    "questions": [
                        {
                            "question": "Who painted the Mona Lisa?",
                            "answer": "Leonardo da Vinci",
                        },
                        {
                            "question": "What are the three primary colors?",
                            "answer": "Red, Blue, and Yellow",
                        },
                        {
                            "question": "What tool is commonly used to blend charcoal in drawing?",
                            "answer": "A blending stump",
                        },
                    ],
                },
            ]
        }
        
        
        current_directory = Path(__file__).parent
        file_path = current_directory / "subjects.json"

        try:
            with open(file_path,'r',encoding='utf-8') as file:
                #created our data file
                self.data = json.load(file)
        except:
            with open(file_path,'w',encoding='utf-8') as file:
                json.dump(starting_file,file,indent=4)
                # list of available cards


                
        
        self.subjects_names = []
        for subject in self.data['subjects']:
            self.subjects_names.append(subject['name'])


        

    def initUI(self):

        self.setWindowTitle("APP NAME")
        self.setGeometry(500,100,800,800)

        self.main_layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()

        # TABS AND MODES AVAILABLE
        self.tabs = QTabWidget()

        self.study_tab = QWidget()
        self.test_tab = QWidget()
        self.create_tab = QWidget()

        # ADD THE TABS
        self.tabs.addTab(self.study_tab,"STUDY")
        self.tabs.addTab(self.test_tab,"TEST")
        self.tabs.addTab(self.create_tab,"CREATE")

        # CREATE THE TABS
        self.create_study_tab()
        self.create_test_tab()
        self.create_create_tab()

        # self.start = QPushButton('Start Studying')
        # self.know_bt= QPushButton("KNOW IT")
        # self.kind_of_know_bt = QPushButton("KIND OF KNOW IT")
        # self.dont_know_bt = QPushButton("DON'T KNOW IT")

        # self.main_layout.addWidget(self.bar)
        # self.main_layout.addWidget(self.image_display)
        # self.main_layout.addWidget(self.start)

        # self.button_layout.addWidget(self.know_bt)
        # self.button_layout.addWidget(self.kind_of_know_bt)
        # self.button_layout.addWidget(self.dont_know_bt)

        # #Connect the buttons to our function
        # self.start.clicked.connect(self.start_studying)
        # self.know_bt.clicked.connect(self.know)
        # self.kind_of_know_bt.clicked.connect(self.kind_of_know)
        # self.dont_know_bt.clicked.connect(self.dont_know)

        # self.main_layout.addLayout(self.button_layout)

        self.main_layout.addWidget(self.tabs)
        self.setLayout(self.main_layout)

        self.setStyleSheet(cozy_style)

    def create_study_tab(self):

        layout = QVBoxLayout()
        study_tab_btn_layout = QHBoxLayout()

        # study tab display
        self.study_tab_question = QLabel("QUESTION")
        self.study_tab_answer = QLabel("ANSWER")
        #LIST OF CARDS COMBO BOX

        
        list_of_cards= QComboBox()
        list_of_cards.addItems(self.subjects_names)
        list_of_cards.setCurrentIndex(-1)
        list_of_cards.setEditable(True)
        list_of_cards.lineEdit().setPlaceholderText("--Select Cards To Study --")


        # study tab button
        self.previous_btn = QPushButton("Previous")
        self.next_btn = QPushButton("Next")
        study_tab_btn_layout.addWidget(self.previous_btn )
        study_tab_btn_layout.addWidget(self.next_btn )

        layout.addWidget(list_of_cards)
        layout.addWidget(self.study_tab_question )
        layout.addWidget(self.study_tab_answer )
        layout.addLayout(study_tab_btn_layout )

        self.study_tab.setLayout(layout)
        
        #combo box activation
        list_of_cards.activated[str].connect(self.study_subject_clicked)
        
    def study_subject_clicked(self,text):
        
        test = []
        for subject in self.data['subjects']:
            if subject['name'] == text:
                test.append(subject)
        # grab the list of questions and answer organize them by date study or date modified 
        # from the date further in the past to the date nearest to the present
        print(test)
        
        

    def create_test_tab(self):
        layout = QVBoxLayout()

        test_tab_button_layout = QHBoxLayout()

        test_tab_display = QLabel("WHAT IS THIS ??")


        
        list_of_cards= QComboBox()
        list_of_cards.addItems(self.subjects_names)
        list_of_cards.setCurrentIndex(-1)
        list_of_cards.setEditable(True)
        list_of_cards.lineEdit().setPlaceholderText("--Select Cards To Study --")

        # study tab button
        previous_btn = QPushButton("Previous")
        next_btn = QPushButton("Next")
        test_tab_button_layout.addWidget(previous_btn )
        test_tab_button_layout.addWidget(next_btn )

        layout.addWidget(list_of_cards)
        layout.addWidget(test_tab_display)

        layout.addLayout(test_tab_button_layout)
        self.test_tab.setLayout(layout)

    def create_create_tab(self):

        layout = QVBoxLayout()

        create_tab_button_layout = QHBoxLayout()

        # create tab input box
        question = QLineEdit('Enter your question') 
        answer = QLineEdit('Enter your answer')


        # create tab buttons

        add_card_bt = QPushButton('Add Card')
        create_new_subject_bt = QPushButton('Create New Subject')
        delete_card_bt = QPushButton('Delete Card')
        

        list_of_cards= QComboBox()
        list_of_cards.addItems(self.subjects_names)
        list_of_cards.setEditable(True)
        list_of_cards.setCurrentIndex(-1)
        list_of_cards.lineEdit().setPlaceholderText("--Select Cards To Study --")
        
        
        layout.addWidget(question)
        layout.addWidget(answer)
        layout.addWidget(list_of_cards)

        create_tab_button_layout.addWidget(add_card_bt)
        create_tab_button_layout.addWidget(delete_card_bt)
        create_tab_button_layout.addWidget(create_new_subject_bt)

        layout.addLayout(create_tab_button_layout)

        self.create_tab.setLayout(layout)

    def start_studying(self):
        # show first question
        self.image_display.setText(self.data[0]['question1'])

    def know(self):
        print("know")

    def kind_of_know(self):
        print("kind if know")

    def dont_know(self):
        print("dont know")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    flash_card = FLASHCARD()
    
    
    flash_card.show()
    
    sys.exit(app.exec_())
