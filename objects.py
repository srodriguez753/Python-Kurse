class Student:

    def __init__(self, name, age, year, salary):
        self.name = name
        self.age = age
        self.year = year
        self.salary = salary

    def __str__(self):
        return f"{self.name}, {self.age}, {self.year}, {self.salary}"


class Student_list:
    def __init__(self):
        self.Student_list = []

    def add_student(self, name, age, year, salary):
        self.Student_list.append(Student(name, age, year, salary))


def main():
    Student_list = Student_list()

    while True:
        print("1. Add")
        print("2. Show")
        choice = input("Choose action: ")

        match choice:
            case "1":
                name = input("Student name: ")
                age = input("Student age: ")
                year = input("Students year: ")
                salary = input("Student salary: ")
