"""
Create a Company of Employees and use OOP to generate classes for types of employees
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.email = self.name + "." + "@email.com"

    def give_raise(self, new_salary):
        self.salary = new_salary


class Developer(Employee):
    def __init__(self, name, salary, languages):
        super().__init__(name, salary)  # Allows reference to our Parent Class
        self.languages = languages   # Generating new variables specific to this class



    def hi(self):
        print(f"{self.name} is my name! Hello!!!")




dev_1 = Developer("James",55555,"python")

dev_1.give_raise(60000)
print(dev_1.salary)
print(f"Dev1: These are the languages i Know is {dev_1.languages}")
