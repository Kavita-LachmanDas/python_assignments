# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet()
#  method returning "Hello from Decorator!". Apply it to a class Person.


# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Apply decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create object and call greet
p = Person("Kavita")
print(p.greet())
