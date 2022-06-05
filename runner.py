from classes.school import School
from classes.student import Student
from classes.person import Person

school = School('Pioneer High')

student_info = {
    'name': 'jake',
    'age': '17',
    'role': 'student',
    'student_id': '201178',
    'password': 'robots',
    'gpa': '3.5'
}

student = Student(**student_info)

print(school.name)
print(student.name)

