# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start().
#  Instantiate the class and access both from outside the class.

class Car:
    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print(f"car brand name is {self.brand} and car has been started....")   

car1 = Car('civic')
print(car1.brand)
car1.start()       