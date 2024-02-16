import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class ContactManagerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.contacts = []

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Contact Manager')
        self.setGeometry(100, 100, 400, 300)  
        self.name_label = QLabel('Name:')
        self.name_entry = QLineEdit()

        self.phone_label = QLabel('Phone:')
        self.phone_entry = QLineEdit()

        self.add_button = QPushButton('Add Contact')
        self.add_button.clicked.connect(self.add_contact)

        self.view_button = QPushButton('View Contacts')
        self.view_button.clicked.connect(self.view_contacts)

        self.search_label = QLabel('Search:')
        self.search_entry = QLineEdit()

        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.search_contact)

        self.delete_button = QPushButton('Delete Contact')
        self.delete_button.clicked.connect(self.delete_contact)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_entry)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_entry)
        layout.addWidget(self.add_button)
        layout.addWidget(self.view_button)
        layout.addWidget(self.search_label)
        layout.addWidget(self.search_entry)
        layout.addWidget(self.search_button)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)

    def add_contact(self):
        name = self.name_entry.text()
        phone = self.phone_entry.text()

        if name and phone.isdigit() and len(phone) == 10:
            contact = {'Name': name, 'Phone': phone}
            self.contacts.append(contact)
            QMessageBox.information(self, 'Success', f"Contact '{name}' added successfully.")
            self.name_entry.clear()
            self.phone_entry.clear()
        else:
            QMessageBox.warning(self, 'Warning', 'Please enter a valid name and a 10-digit phone number.')

    def view_contacts(self):
        if self.contacts:
            contacts_text = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in self.contacts])
            QMessageBox.information(self, 'Contact List', f"Contact List:\n{contacts_text}")
        else:
            QMessageBox.information(self, 'Contact List', 'Contact list is empty.')

    def search_contact(self):
        search_term = self.search_entry.text().lower()
        matching_contacts = [contact for contact in self.contacts if search_term in contact['Name'].lower() or search_term in contact['Phone']]
        if matching_contacts:
            contacts_text = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in matching_contacts])
            QMessageBox.information(self, 'Search Results', f"Search Results:\n{contacts_text}")
        else:
            QMessageBox.information(self, 'Search Results', 'No matching contacts found.')

    def delete_contact(self):
        name_to_delete = self.name_entry.text()
        if name_to_delete:
            for contact in self.contacts:
                if contact['Name'] == name_to_delete:
                    self.contacts.remove(contact)
                    QMessageBox.information(self, 'Success', f"Contact '{name_to_delete}' deleted successfully.")
                    self.name_entry.clear()
                    self.phone_entry.clear()
                    return
            QMessageBox.warning(self, 'Warning', f"Contact '{name_to_delete}' not found.")
        else:
            QMessageBox.warning(self, 'Warning', 'Please enter the name of the contact to delete.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    contact_manager_app = ContactManagerApp()
    contact_manager_app.show()
    sys.exit(app.exec_())
