class Calculator:
    count = 0  # Static attribute to count the number of calls to add()

    @staticmethod
    def add(a, b):
        Calculator.count += 1  # Increment count each time add() is called
        return a + b

# Demonstration of using the add() method and tracking the count
result1 = Calculator.add(5, 10)
print(f"Result of first addition: {result1}")
print(f"Add method called: {Calculator.count} time(s)")

result2 = Calculator.add(20, 30)
print(f"Result of second addition: {result2}")
print(f"Add method called: {Calculator.count} time(s)")
