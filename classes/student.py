from classes.person import Person

class Student(Person):
    def __init__(self, name, age, role, student_id, password, gpa):
        super().__init__(name=name, age=age, role=role, password=password)
        self.student_id = student_id
        self.gpa = gpa

    @classmethod
    def load_all_students(cls):
        return super().load_all_people('../data/students.csv')

    def __str__(self):
        return f'Student: {self.name}, ID: {self.student_id}, GPA: {self.gpa}'
