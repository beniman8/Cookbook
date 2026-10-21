import sys

# Ignore the deprecation warnings
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

from data import save_data, get_current_data, edit_data, delete_data,edit_all_data



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


from helper import FormDialog




from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QComboBox,
    QVBoxLayout,
    QListWidget,
    QInputDialog,
    QDialog,
    QListWidgetItem,
    QPushButton
    
)

from PyQt5.QtCore import Qt
class APP(QWidget):

    def __init__(self):
        super().__init__()
        
  
        self.contacts= get_current_data()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("CONTACT BOOK")
        self.setGeometry(500, 100, 800, 800)

        self.main_layout = QVBoxLayout()

        self.image_display = QLabel("Contacts")
        
        self.contact_list = QListWidget()
        
        self.contact_form = FormDialog()
        
        self.add_button= QPushButton('Add Contact')
        
        
        self.add_button.clicked.connect(self.add_contact)

        self.contact_list.itemClicked.connect(self.on_item_clicked)
    
    
        self.main_layout.addWidget(self.image_display)
       
        self.update_contact_list()
       
        self.main_layout.addWidget(self.add_button)


        self.setLayout(self.main_layout)

        self.setStyleSheet(cozy_style)
        
    def on_item_clicked(self, item):
        # Retrieve the tuple using data()
        user_id, user_name = item.data(Qt.UserRole)

        data =get_current_data()
        for value in data['contacts']:
            if value['user_id']== user_id:
            
                data=value
    
        self.contact_form.set_form_data(data['first_name'],data['last_name'],data['phone_number'],data['email'],data['address'],data['instagram'])
        
        
        if self.contact_form.exec_() == QDialog.Accepted:
            # Retrieve the user inputs if OK was pressed
            form_data = self.contact_form.get_form_data()

            edit_all_data(user_id,form_data['first_name'],form_data['last_name'],form_data['phone_number'],form_data['email'],form_data['address'],form_data['instagram'])


            
            print("DataBase updated Successfully!")
            self.contact_list.clear()   
            self.main_layout.removeWidget(self.contact_list) 
            
            #DONE TELL PROGram we have a new value we need to use for the program 
            self.contacts = get_current_data()
            
            self.update_contact_list()
        else:
            print("User canceled the dialog.")
            
            
            


        
            

    def update_contact_list(self):
        self.contacts = get_current_data()
        
        self.contact_list.clear()
        
        for value in self.contacts['contacts']:

            # 1. Create a QListWidgetItem with a primary display label
            item = QListWidgetItem(value['first_name'])
            
            # 2. Store two values (e.g., ID and extra metadata) using setData
            two_values = (value['user_id'],value['last_name'])
            item.setData(Qt.UserRole, two_values)
            
            self.contact_list.addItem(item)
        
        
        self.main_layout.addWidget(self.contact_list)

    def add_contact(self):

        # Clear the form
        self.contact_form.set_form_data(
            "", "", "", "", "", ""
        )

        # Open the dialog
        if self.contact_form.exec_() == QDialog.Accepted:

            form_data = self.contact_form.get_form_data()

            save_data(
                form_data['first_name'],
                form_data['last_name'],
                form_data['phone_number'],
                form_data['email'],
                form_data['address'],
                form_data['instagram']
            )

            # Refresh the list
            self.update_contact_list()

            print("Contact added successfully!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    application = APP()

    application.show()

    sys.exit(app.exec_())
