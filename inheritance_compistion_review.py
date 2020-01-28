# Here's another review on Inheritance vs Composition
# Inheritance (Is-A Relationship) A dog is an Animal A horse is a Animal
# Composition (has-A Relationship) A dog has a Tail A horse has a tail

# We're going to do an example where HR system needs to process payroll for the company’s employees,
# but there are different types of employees depending on how their payroll is calculated.


class Payroll_system:
    def calculate_payroll(self,employees):
        print("Calculating Payroll...")
        print("=====================")
        for employee in employees:
            print(f"The Payroll for {employee.id} - {employee.name}")
            print(f"Is {employee.calculate_payroll()}")


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return.self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hourly_wage)
        super().__init__(self, id, name)
        self.hourly_wage = hourly_wage

    def calculate_payroll(self):
        return self.hourly_wage


class CommissionedEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission)
        super().__init__(self,id,name,weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed_salary = super().calculate_payroll(Sal
