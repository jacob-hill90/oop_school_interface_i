import csv
from classes.school import School
from classes.person import Person

class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        Person.__init__(self, name, age, password, role)
        self.school_id = school_id

    def __str__(self):
        return f'{self.name} is a {self.role} her id is {self.school_id}'
    
    def all_students():
        with open("data/students.csv", "r") as student_file:
            reader = csv.DictReader(student_file)
            arr_students = []
            for row in reader:
                arr_students.append(Student(**row))
        
        return arr_students
