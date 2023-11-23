class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):  
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            Overtime_amount = (overtime * (self.emp_salary/50))
            Sum_salary = self.emp_salary + Overtime_amount
        else:
            Sum_salary = self.emp_salary
        return Sum_salary

    def assign_department(self, New_emp_department):
        self.emp_department = New_emp_department

    def print_employee_details(self):
        print (f"Employee Name : {self.emp_name}")
        print (f"Employee ID : {self.emp_id}")
        print (f"Employee Salary : {self.emp_salary}")
        print (f"Employee Department : {self.emp_department}")

employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
employee3 = Employee("MARTIN", "E7900", 50000, "SALES")
employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

employee4.print_employee_details()
employee4.assign_department("7-11")
print("NEW Department:", employee1.emp_department)
salary = employee4.calculate_emp_salary(60)
print("Calculate salary:", salary)