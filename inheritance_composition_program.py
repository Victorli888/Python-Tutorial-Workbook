import inheritance_compistion_review
# Now that I've imported the functions I needed from inheritance_compisition_review I can call upon the functions I
# in that file...

salary_employee = inheritance_compistion_review.SalaryEmployee(775001, 'Andrew Yang', 2200)
hourly_employee = inheritance_compistion_review.HourlyEmployee(775002, 'Elizabeth', 15)
commission_employee = inheritance_compistion_review.CommissionedEmployee(775003, 'Joe Biden', 2000, 199)

# Now that I've imported and created usable variables... lets start calculating peoples payrolls

payroll_system = inheritance_compistion_review.PayrollSystem()
payroll_system.calculate_payroll([salary_employee, hourly_employee, commission_employee])
