class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = int(salary)  # Ensure the salary is an integer for calculations

class Payroll:
    def __init__(self):
        self.employees = []  # This will store a list of Employee objects

    def add_employee(self, employee):
        self.employees.append(employee)  # Adds the Employee object to the list

    def total_payroll(self):
        # Sum all employee salaries in the list
        return sum(employee.salary for employee in self.employees)

# Create Employee objects
emp1 = Employee("Bob", "40000")  # Note that salary is passed as a string, but converted to an int
emp2 = Employee("Jane", "50000")

# Create a Payroll object
payroll1 = Payroll()

# Add Employee objects to the Payroll object
payroll1.add_employee(emp1)
payroll1.add_employee(emp2)

# Calculate total payroll
print(f"Total Payroll: {payroll1.total_payroll()}")  # Outputs: Total Payroll: 90000
