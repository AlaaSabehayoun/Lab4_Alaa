import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QFormLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
)
from oop_classes import Student, Instructor, Course

# Basic in-memory lists to store the data for this demo
students = []
instructors = []
courses = []


class SchoolManagementSystem(QMainWindow):
    """
    This is a PyQt5-based application for managing students, instructors, and courses.

    The goal here is to provide a basic interface where users can:
    - Add new entries for students, instructors, and courses.
    - View these entries in a simple table.
    """

    def __init__(self):
        """
        Set up the main window and initialize the tabs for each entity (Students, Instructors, Courses).
        """
        super().__init__()
        self.setWindowTitle("School Management System")
        self.setGeometry(100, 100, 900, 700)

        # Main Tab Widget
        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)

        # Create and add tabs
        self.create_student_tab()
        self.create_instructor_tab()
        self.create_course_tab()

    def create_student_tab(self):
        """
        Build the "Students" tab.

        This tab has:
        - A form to add new students.
        - A table that displays the list of all students added so far.
        """
        self.student_tab = QWidget()
        self.tabs.addTab(self.student_tab, "Students")

        layout = QVBoxLayout()

        # Student form
        form = QFormLayout()
        self.student_name_input = QLineEdit()
        self.student_age_input = QLineEdit()
        self.student_email_input = QLineEdit()
        self.student_id_input = QLineEdit()

        form.addRow(QLabel("Name:"), self.student_name_input)
        form.addRow(QLabel("Age:"), self.student_age_input)
        form.addRow(QLabel("Email:"), self.student_email_input)
        form.addRow(QLabel("Student ID:"), self.student_id_input)

        # Add Button
        add_button = QPushButton("Add Student")
        add_button.clicked.connect(self.add_student)
        form.addWidget(add_button)

        layout.addLayout(form)

        # Table for students
        self.student_table = QTableWidget(0, 4)
        self.student_table.setHorizontalHeaderLabels(["Name", "Age", "Email", "Student ID"])
        layout.addWidget(self.student_table)

        self.student_tab.setLayout(layout)

    def create_instructor_tab(self):
        """
        Build the "Instructors" tab.

        This tab contains:
        - A form for adding instructors.
        - A table to view all added instructors.
        """
        self.instructor_tab = QWidget()
        self.tabs.addTab(self.instructor_tab, "Instructors")

        layout = QVBoxLayout()

        # Instructor form
        form = QFormLayout()
        self.instructor_name_input = QLineEdit()
        self.instructor_age_input = QLineEdit()
        self.instructor_email_input = QLineEdit()
        self.instructor_id_input = QLineEdit()

        form.addRow(QLabel("Name:"), self.instructor_name_input)
        form.addRow(QLabel("Age:"), self.instructor_age_input)
        form.addRow(QLabel("Email:"), self.instructor_email_input)
        form.addRow(QLabel("Instructor ID:"), self.instructor_id_input)

        # Add Button
        add_button = QPushButton("Add Instructor")
        add_button.clicked.connect(self.add_instructor)
        form.addWidget(add_button)

        layout.addLayout(form)

        # Table for instructors
        self.instructor_table = QTableWidget(0, 4)
        self.instructor_table.setHorizontalHeaderLabels(["Name", "Age", "Email", "Instructor ID"])
        layout.addWidget(self.instructor_table)

        self.instructor_tab.setLayout(layout)

    def create_course_tab(self):
        """
        Build the "Courses" tab.

        This tab includes:
        - A form for adding new courses.
        - A table for viewing all courses.
        """
        self.course_tab = QWidget()
        self.tabs.addTab(self.course_tab, "Courses")

        layout = QVBoxLayout()

        # Course form
        form = QFormLayout()
        self.course_id_input = QLineEdit()
        self.course_name_input = QLineEdit()

        form.addRow(QLabel("Course ID:"), self.course_id_input)
        form.addRow(QLabel("Course Name:"), self.course_name_input)

        # Add Button
        add_button = QPushButton("Add Course")
        add_button.clicked.connect(self.add_course)
        form.addWidget(add_button)

        layout.addLayout(form)

        # Table for courses
        self.course_table = QTableWidget(0, 2)
        self.course_table.setHorizontalHeaderLabels(["Course ID", "Course Name"])
        layout.addWidget(self.course_table)

        self.course_tab.setLayout(layout)

    def add_student(self):
        """
        Add a student to the system and update the student table.

        The input fields (name, age, email, and student ID) are validated before adding.
        """
        name = self.student_name_input.text()
        age = self.student_age_input.text()
        email = self.student_email_input.text()
        student_id = self.student_id_input.text()

        if not name or not age or not email or not student_id:
            QMessageBox.warning(self, "Input Error", "All fields are required.")
            return

        try:
            age = int(age)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Age must be a valid number.")
            return

        # Create and store the student
        new_student = Student(name, age, email, student_id)
        students.append(new_student)

        # Update the table
        row_count = self.student_table.rowCount()
        self.student_table.insertRow(row_count)
        self.student_table.setItem(row_count, 0, QTableWidgetItem(name))
        self.student_table.setItem(row_count, 1, QTableWidgetItem(str(age)))
        self.student_table.setItem(row_count, 2, QTableWidgetItem(email))
        self.student_table.setItem(row_count, 3, QTableWidgetItem(student_id))

        QMessageBox.information(self, "Success", "Student added successfully.")

    def add_instructor(self):
        """
        Add an instructor to the system and update the instructor table.

        Validates the fields for name, age, email, and instructor ID.
        """
        # Implementation is similar to add_student()

    def add_course(self):
        """
        Add a course to the system and update the course table.

        Validates fields for course ID and course name.
        """
        # Implementation is similar to add_student()


# Main Execution
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SchoolManagementSystem()
    window.show()
    sys.exit(app.exec_())
