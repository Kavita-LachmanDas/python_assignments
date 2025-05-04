# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, _salary, __ssn):
        self.name = name              # Public variable
        self._salary = _salary        # Protected variable
        self.__ssn = __ssn            # Private variable

        print("Inside class:")
        print(f"Public: {self.name}")
        print(f"Protected: {self._salary}")
        print(f"Private: {self.__ssn}")  # Accessible inside the class

# Create an object
employee = Employee('Kavita', 1200000000, 'readonly')

print("\nOutside class:")
# Access public
print("Public:", employee.name)

# Access protected
print("Protected:", employee._salary)

# Access private (this will raise an error if you try: employee.__ssn)
# So instead, use name mangling:
print("Private (accessed via name mangling):", employee._Employee__ssn)
