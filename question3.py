# Base class
class Animal:
    def eat(self):
        print("The animal is eating.")

    def sleep(self):
        print("The animal is sleeping.")

# Subclass
class Dog(Animal):
    def bark(self):
        print("The dog is barking.")

# Demonstration of using both inherited and new methods
my_dog = Dog()

# Using inherited methods
my_dog.eat()
my_dog.sleep()

# Using the new method
my_dog.bark()
