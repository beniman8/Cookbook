import sys  
import json 
from pathlib import Path 
from datetime import datetime
from PyQt5.QtGui import QFont

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
        self.file_path = current_directory / "subjects.json"

        try:
            with open(self.file_path,'r',encoding='utf-8') as file:
                #created our data file
                self.data = json.load(file)
        except:
            with open(self.file_path,'w',encoding='utf-8') as file:
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

        self.main_layout.addWidget(self.tabs)
        self.setLayout(self.main_layout)

        self.setStyleSheet(cozy_style)

    def create_study_tab(self):

        layout = QVBoxLayout()
        study_tab_btn_layout = QHBoxLayout()


        font = QFont("Arial",24)
        # study tab display
        self.study_tab_question = QLabel("QUESTION")
        self.study_tab_answer = QLabel("ANSWER")
        
        self.study_tab_question.setFont(font)
        self.study_tab_answer.setFont(font)
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
        
        #connect button to function
        self.next_btn.clicked.connect(self.next_question)
        self.previous_btn.clicked.connect(self.previous_question)
        
    def study_subject_clicked(self,text):
        #TODO delete old text object when you create a new text object
        
        
        self.study_data = []
        for subject in self.data['subjects']:
            if subject['name'] == text:
                self.study_data.append(subject)
        
        # #sort the study data
        # TODO FIGURE OUT HOW TO SORT THE DATA
        # by_date = sorted(self.study_data,key= lambda date:date['date_studied'])
        
        self.questions =  []
        self.answers  = [] 
        self.current_data_len=0
        self.len_of_questions = len( self.study_data[0]['questions']) - 1
        
        for  info in  self.study_data[0]['questions']:
            self.questions.append(info['question'])
            self.answers.append(info['answer'])
            
        self.study_data[0]['questions'][self.current_data_len]['date_studied'] = datetime.now().isoformat()
        

        self.study_tab_question.setText(self.questions[self.current_data_len])
        self.study_tab_answer.setText(self.answers[self.current_data_len])
        
        

        
    def next_question(self):
        #only add when it is smaller than length of questions
        if self.current_data_len < self.len_of_questions:
            self.current_data_len+=1

        self.study_tab_question.setText(self.questions[self.current_data_len])
        self.study_tab_answer.setText(self.answers[self.current_data_len])
        self.study_data[0]['questions'][self.current_data_len]['date_studied'] = datetime.now().isoformat()
        
        
        with open(self.file_path, "w") as f:
            json.dump(self.data, f, indent=4)

        
        
    def previous_question(self):
        
        if abs(self.current_data_len) <= self.len_of_questions:
            self.current_data_len-=1 
            
        
            
        self.study_tab_question.setText(self.questions[self.current_data_len])
        self.study_tab_answer.setText(self.answers[self.current_data_len])  

        self.study_tab_question.setText(self.questions[self.current_data_len])
        self.study_tab_answer.setText(self.answers[self.current_data_len])
        self.study_data[0]['questions'][self.current_data_len]['date_studied'] = datetime.now().isoformat()
        
        
        with open(self.file_path, "w") as f:
            json.dump(self.data, f, indent=4)
        
        

    def create_test_tab(self):
        layout = QVBoxLayout()

        test_tab_button_layout = QHBoxLayout()

        self.test_tab_display = QLabel("WHAT IS THIS ??")

        

        
        list_of_cards= QComboBox()
        list_of_cards.addItems(self.subjects_names)
        list_of_cards.setCurrentIndex(-1)
        list_of_cards.setEditable(True)
        list_of_cards.lineEdit().setPlaceholderText("--Select Cards To Study --")

        # study tab button
        know_btn = QPushButton("Know")
        kind_know_btn = QPushButton("Kind of Know")
        dont_know_btn = QPushButton("Don't Know")
        
        test_tab_button_layout.addWidget(know_btn)
        test_tab_button_layout.addWidget(kind_know_btn)
        test_tab_button_layout.addWidget(dont_know_btn)
        

        layout.addWidget(list_of_cards)
        layout.addWidget(self.test_tab_display)

        layout.addLayout(test_tab_button_layout)
        self.test_tab.setLayout(layout)
        #combo box activation
        
        know_btn.clicked.connect(self.know)
        dont_know_btn.clicked.connect(self.dont_know)
        kind_know_btn.clicked.connect(self.kind_of_know)

        
        list_of_cards.activated[str].connect(self.start_studying)



    def start_studying(self,text):
        #TODO delete old text object when you create a new text object
        
        
        self.test_data = []
        for subject in self.data['subjects']:
            if subject['name'] == text:
                self.test_data.append(subject)
            
        self.questions =  []
        self.answers  = [] 
        self.current_data_len=0
        self.len_of_questions = len(self.test_data[0]['questions']) - 1
        
        for  info in self.test_data[0]['questions']:
            self.questions.append(info['question'])

        self.test_tab_display.setText(self.questions[self.current_data_len])
        
        
        
    def know(self):
        self.test_tab_display.setText(self.questions[self.current_data_len])
        
        self.test_data[0]['questions'][self.current_data_len]['knowledge_level'] = 2   

        if self.current_data_len < self.len_of_questions:
            self.current_data_len +=1
            

        
        with open(self.file_path, "w") as f:
            json.dump(self.data, f, indent=4)
        
    


    def kind_of_know(self):
        self.test_tab_display.setText(self.questions[self.current_data_len])
        
        self.test_data[0]['questions'][self.current_data_len]['knowledge_level'] = 1   

        if self.current_data_len < self.len_of_questions:
            self.current_data_len +=1
            

        
        with open(self.file_path, "w") as f:
            json.dump(self.data, f, indent=4)

    def dont_know(self):
        self.test_tab_display.setText(self.questions[self.current_data_len])
        
        self.test_data[0]['questions'][self.current_data_len]['knowledge_level'] = 0   

        if self.current_data_len < self.len_of_questions:
            self.current_data_len +=1
            

        
        with open(self.file_path, "w") as f:
            json.dump(self.data, f, indent=4) 
        
        
        
        
        


    def create_create_tab(self):

        layout = QVBoxLayout()

        create_tab_button_layout = QHBoxLayout()

        # create tab input box
        self.question = QLineEdit('Enter your question') 
        self.answer = QLineEdit('Enter your answer')

        #subject name 
        self.new_subject_name= QInputDialog()
        # create tab buttons

        add_question_bt = QPushButton('Add Question')
        create_new_subject_bt = QPushButton('Create New Subject')
      
        

        list_of_cards= QComboBox()
        list_of_cards.addItems(self.subjects_names)
        list_of_cards.setEditable(True)
        list_of_cards.setCurrentIndex(-1)
        list_of_cards.lineEdit().setPlaceholderText("--Select Cards To Study --")
        
        
        layout.addWidget(self.question)
        layout.addWidget(self.answer)
        layout.addWidget(list_of_cards)

        create_tab_button_layout.addWidget(add_question_bt)
        create_tab_button_layout.addWidget(create_new_subject_bt)

        layout.addLayout(create_tab_button_layout)

        self.create_tab.setLayout(layout)
        
        create_new_subject_bt.clicked.connect(self.create_new_subject)
        add_question_bt.clicked.connect(lambda:self.add_question(list_of_cards.currentIndex()))
        
    def add_question(self,ind):
        #clear fields and reset combobox
    
        question_and_answer = {'question':self.question.text(),'answer':self.answer.text(),'date_studied':datetime.now().isoformat(),'knowledge_level':0}
        self.data['subjects'][ind]['questions'].append(question_and_answer)
        
        with open(self.file_path, "w") as f:
            json.dump(self.data, f, indent=4) 
            
    def create_new_subject(self):
        
        subject_name , ok = self.new_subject_name.getText(self,"Subject Name","Enter new name:")
        
        
        if ok:
            self.data['subjects'].append( {"name": subject_name,"questions": []})
            with open(self.file_path, "w") as f:
                json.dump(self.data, f, indent=4) 




if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    flash_card = FLASHCARD()
    
    
    flash_card.show()
    
    sys.exit(app.exec_())
