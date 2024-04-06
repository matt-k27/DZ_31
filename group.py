from exceptions import GroupMaximumAmountError
from student import Student


class Group:
    maxStudents = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.maxStudents:
            raise GroupMaximumAmountError()
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        temp = self.find_student(last_name)
        if temp is not None:
            self.group.remove(temp)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += student.__str__() + '\n'
        return f'Number:{self.number}\n{all_students} '

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Not a Student object")
        else:
            if self.__str__() != other.__str__():
                raise ValueError("Not equal")
            else:
                return True