import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QMessageBox

class ToDoListApp(QWidget):
    def __init__(self):
        super().__init__()

        self.tasks = []

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('To-Do List App')
        self.setGeometry(100, 100, 400, 300)

        self.task_entry = QLineEdit()
        self.add_button = QPushButton('Add Task')
        self.add_button.clicked.connect(self.add_task)

        self.show_incomplete_button = QPushButton('Show Incomplete Tasks')
        self.show_incomplete_button.clicked.connect(self.show_incomplete_tasks)

        self.task_list = QListWidget()
        self.task_list.itemClicked.connect(self.update_task_status)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.task_entry)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.show_incomplete_button)
        self.layout.addWidget(self.task_list)

        self.setLayout(self.layout)

    def add_task(self):
        task_text = self.task_entry.text()
        if task_text:
            self.tasks.append({'text': task_text, 'completed': False})
            self.update_task_list()
            self.task_entry.clear()
        else:
            QMessageBox.warning(self, 'Warning', 'Please enter a task.')

    def update_task_list(self):
        self.task_list.clear()
        for task in self.tasks:
            status_icon = '✔' if task['completed'] else '◻'
            task_item = f"{status_icon} {task['text']}"
            self.task_list.addItem(task_item)

    def update_task_status(self, task_item):
        index = self.task_list.row(task_item)
        self.tasks[index]['completed'] = not self.tasks[index]['completed']
        self.update_task_list()

    def show_incomplete_tasks(self):
        incomplete_tasks = [task['text'] for task in self.tasks if not task['completed']]
        if incomplete_tasks:
            tasks_text = '\n'.join(incomplete_tasks)
            QMessageBox.information(self, 'Incomplete Tasks', f"Incomplete Tasks:\n{tasks_text}")
        else:
            QMessageBox.information(self, 'Incomplete Tasks', 'No incomplete tasks.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_list_app = ToDoListApp()
    todo_list_app.show()
    sys.exit(app.exec_())
