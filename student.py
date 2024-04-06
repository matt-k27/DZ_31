from human import Human


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, {self.record_book}"

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Not a Student object")
        else:
            if self.__str__() != other.__str__():
                raise ValueError("Not equal")
            else:
                return True

    def __hash__(self):
        return hash(str(self))