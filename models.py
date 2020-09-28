class Person(object):
    def __init__(self, age, name):
        self._age = age
        self._name = name

    def __str__(self):
        return f"{self._name}/{self._age} лет"

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name


class Student(Person):
    def __init__(self, age, name, group):
        super().__init__(age, name)
        self.__marks = []
        self.__group = group

    def __str__(self):
        return f'Student {self.__group} {super().__str__()}'

    def get_group(self):
        return self.__group

    def set_group(self, new_group):
        self.__group = new_group
        print(f"group changed to {self.__group}")

    def get_marks(self):
        return self.__marks

    def add_mark(self, mark: int):
        self.__marks.append(mark)


class Employee(Person):
    def __init__(self, age, name, position, salary):
        super().__init__(age, name)
        self._position = position
        self._salary = salary

    def __str__(self):
        return f'Employee {self._position} {super().__str__()}'

    def get_position(self):
        return self._position

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary: int):
        self._salary = new_salary


class Teacher(Employee):
    def __init__(self, age, name, salary):
        super().__init__(age, name, 'Teacher', salary)

    def __str__(self):
        return f'Teacher {Person.__str__(self)}'

    def set_marks(self, student: Student, mark: int):
        student.add_mark(mark)

