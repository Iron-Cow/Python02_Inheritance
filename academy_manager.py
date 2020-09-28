from models import *


class AcademyManager(object):
    def test_academy(self):
        person = Person(16, 'Yura')
        print(person)
        print(person.get_name())
        print(person.get_age())


        student1 = Student(17, 'Ivan', 'Python666')
        print(student1)
        print(student1.get_group())
        student1.set_group('Python_02')
        print(student1.get_group())

        student1.add_mark(12)
        student1.add_mark(11)
        student1.add_mark(11)
        student1.add_mark(11)
        student1.add_mark(12)

        print(student1.get_marks())

        new_emp = Employee(55, 'Borys', 'Teacher', 100500)
        print(new_emp)
        print(new_emp.get_salary())
        print(new_emp.get_name())
        print(new_emp.get_position())
        new_emp.set_salary(5000)
        print(new_emp.get_salary())

        teacher1 = Teacher(55, 'Oleg', 6000)
        print(teacher1)
        print(teacher1.get_salary())

        teacher1.set_marks(student1, 7)
        print(student1.get_marks())
        print(teacher1.__repr__())

