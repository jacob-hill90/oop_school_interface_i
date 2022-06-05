from classes.person import Person

class Student(Person):
    def __init__(self, name, age, role, student_id, password, gpa):
        super().__init__(name=name, age=age, role=role, password=password)
        self.student_id = student_id
        self.gpa = gpa
