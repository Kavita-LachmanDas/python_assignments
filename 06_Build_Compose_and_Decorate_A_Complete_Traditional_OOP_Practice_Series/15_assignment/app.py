# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.


class A:
    def show(self):
        print("Show method from Class A")

class B(A):
    def show(self):
        print("Show method from Class B")

class C(A):
    def show(self):
        print("Show method from Class C")

class D(B, C):  # Diamond inheritance
    pass

d = D()
d.show()

# Print Method Resolution Order
print(D.__mro__)
