from classes.school import School

school = School('Pioneer High')

print(school.name)

for student_info in school.students:
    print(student_info)

for staff_info in school.staff:
    print(staff_info)
