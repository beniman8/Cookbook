import sys

from PyQt5.QtWidgets import (
    QDialog,
    QFormLayout,
    QLineEdit,
    QSpinBox,
    QComboBox,
    QDialogButtonBox,
    QVBoxLayout,
    QLabel
)
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

class FormDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("User Information Form")
        self.resize(350, 180)
        self.setStyleSheet(cozy_style)
        
        # 1. Create form elements (widgets)
        

        self.first_name= QLineEdit() 
        self.first_name.setFixedSize(600,50)
        self.last_name= QLineEdit()
        self.phone_number= QLineEdit()
        self.email= QLineEdit()
        self.address= QLineEdit()
        self.instagram= QLineEdit()


        
        # 2. Arrange widgets inside a QFormLayout
        form_layout = QFormLayout()
        form_layout.addRow('First Name', self.first_name)
        form_layout.addRow("Last Name:", self.last_name)
        form_layout.addRow("Phone Number:", self.phone_number)
        form_layout.addRow("Email:", self.email)
        form_layout.addRow("Home Address :", self.address)
        form_layout.addRow("Instagram:", self.instagram)


        # 3. Add standard OK / Cancel buttons
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        
        # Connect button signals to built-in slot logic
        self.button_box.accepted.connect(self.accept)  # Closes dialog and returns QDialog.Accepted
        self.button_box.rejected.connect(self.reject)  # Closes dialog and returns QDialog.Rejected
        
        # 4. Compile everything into a main vertical layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.button_box)
        self.setLayout(main_layout)

    def get_form_data(self):
        """Helper method to easily extract data from the completed form."""
        return {

            "first_name": self.first_name.text(),
            "last_name": self.last_name.text(),
            "phone_number": self.phone_number.text(),
            "email": self.email.text(),
            "address": self.address.text(),
            "instagram": self.instagram.text(),

        }
        
    def set_form_data(self,first_name,last_name,phone_number,email,address,instagram):
        
        self.first_name.setText(first_name ) 
        self.last_name.setText(last_name )
        self.phone_number.setText(phone_number) 
        self.email.setText(email) 
        self.address.setText(address) 
        self.instagram.setText(instagram) 