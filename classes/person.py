import csv
import os

class Person:
    def __init__(self, name, age, password, role): 
        self.name = name 
        self.age = age         
        self.password = password
        self.role = role

    @classmethod
    def load_all_people(cls, file_name):
        all_people = []

        my_path = os.path.abspath(os.path.dirname(__file__))
        file = os.path.join(my_path, file_name)
        with open(file, mode='r') as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for row_dict in dict_reader:
                person = cls(**row_dict)
                all_people.append(person)
        
        return all_people
                
