# Base class
class Employee:
    def calculate_salary(self):
        print("Calculating salary for an employee.")

# Subclass
class Manager(Employee):
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        total_salary = self.base_salary + self.bonus
        print(f"Calculating salary for manager: Base Salary = {self.base_salary}, Bonus = {self.bonus}, Total = {total_salary}")

# Demonstration of overridden behavior
# Create an instance of Employee
employee = Employee()
employee.calculate_salary()  # Expected output: "Calculating salary for a generic employee."

# Create an instance of Manager
manager = Manager(base_salary=50000, bonus=10000)
manager.calculate_salary()  # Expected output: Detailed salary calculation for a manager
