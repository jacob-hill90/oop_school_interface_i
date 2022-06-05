from classes.person import Person

class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name=name, age=age, password=password, role=role)
        self.employee_id = employee_id

    @classmethod
    def load_all_staff(cls):
        return super().load_all_people('../data/staff.csv')

    def __str__(self):
        return f'Staff: {self.name}, ID: {self.employee_id}, Age: {self.age}'
