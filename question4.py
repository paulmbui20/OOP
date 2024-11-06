class Cat:
    def make_sound(self):
        print("Meow")

class Dog:
    def make_sound(self):
        print("Woof")

# Function to demonstrate polymorphism
def animal_sound(animal):
    animal.make_sound()

# Create instances of Cat and Dog
my_cat = Cat()
my_dog = Dog()

# Demonstrate polymorphism by passing both instances to the same function
animal_sound(my_cat)  # Output: Meow
animal_sound(my_dog)  # Output: Woof
