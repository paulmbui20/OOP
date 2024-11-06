class Rectangle:
    def __init__(self, width, height=None):
        # If only one argument is provided, assume it's a square
        if height is None:
            self.width = width
            self.height = width
        else:
            self.width = width
            self.height = height

    def area(self):
        return self.width * self.height

# Test cases
# Create a square with side length 5
square = Rectangle(5)
print(f"Square area: {square.area()}")  # Expected output: 25

# Create a rectangle with width 4 and height 6
rectangle = Rectangle(4, 6)
print(f"Rectangle area: {rectangle.area()}")  # Expected output: 24
