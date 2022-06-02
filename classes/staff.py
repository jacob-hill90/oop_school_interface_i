import csv
from classes.school import School
from classes.person import Person

class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
        Person.__init__(self, name, age, password, role)
        self.employee_id = employee_id