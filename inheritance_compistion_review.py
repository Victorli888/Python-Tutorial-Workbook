# Here's another review on Inheritance vs Composition
# Inheritance (Is-A Relationship) A dog is an Animal A horse is a Animal
# Composition (has-A Relationship) A dog has a Tail A horse has a tail

# We're going to do an example where HR system needs to process payroll for the company’s employees,
# but there are different types of employees depending on how their payroll is calculated.

class Employee:    # This is Base class that all the other classes will refrence to
    #  For example, All employee have an ID and Name (Has-A)
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PayrollSystem:
    def calculate_payroll(self, employees):
        print("Calculating Payroll...")
        print("=====================")
        for employee in employees:
            print(f"The Payroll for {employee.id} - {employee.name}")
            print(f"Is {employee.calculate_payroll()}")


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name) # Has-A id and Name
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):  # Is-A Employee
    def __init__(self, id, name, hourly_wage):
        super().__init__(id, name)  # has an ID and Name
        self.hourly_wage = hourly_wage

    def calculate_payroll(self):
        return self.hourly_wage


class CommissionedEmployee(SalaryEmployee):  # Is-A SalaryEmployee
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)  # Has-A ID, Name, and Weekly_Salary
        self.commission = commission

    def calculate_payroll(self):
        fixed_salary = super().calculate_payroll()
        # Has-A relationship with SalaryEmployee in terms of calculate.payroll
        return fixed_salary + self.commission
