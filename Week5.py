# Assignment 1
# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        return f"{self.brand} {self.model} is calling {number}..."

    def specs(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage"

# Derived class 1
class AndroidPhone(Smartphone):
    def feature(self):  # Polymorphic method
        return f"{self.brand} {self.model} is running on Android"

# Derived class 2
class iPhone(Smartphone):
    def feature(self):  # Polymorphic method
        return f"{self.brand} {self.model} is running on iOS"

# Create objects
s1 = AndroidPhone("Samsung", "Galaxy S24", 256)
s2 = iPhone("Apple", "iPhone 15", 512)

# Polymorphism in action
for phone in [s1, s2]:
    print(phone.specs())
    print(phone.feature())
    print(phone.call("+123456789"))
 
    
# Activity 2
class Dog:
    def move(self):
        return "Running!"

class Fish:
    def move(self):
        return "Swimming!"
    
class Bird:
    def move(self):
        return "Flying!"

# Polymorphism in action
for animal in [Dog(), Fish(), Bird()]:
    print(animal.move())