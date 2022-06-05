from classes.student import Student
from classes.staff import Staff

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.load_all_staff()
        self.students = Student.load_all_students()

