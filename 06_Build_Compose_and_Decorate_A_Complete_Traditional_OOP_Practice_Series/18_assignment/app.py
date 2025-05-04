# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. 
# Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.


class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # private attribute
    
    # @property to get the value of _price
    @property
    def price(self):
        return self._price
    
    # @price.setter to update the value of _price
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative.")
        else:
            self._price = value
    
    # @price.deleter to delete the _price attribute
    @price.deleter
    def price(self):
        print(f"Price of {self.name} is being deleted.")
        del self._price

product1 = Product("Laptop", 100000)

# Get price using the property decorator
print(f"Initial Price: {product1.price}")

# Set price using the setter
product1.price = 120000
print(f"Updated Price: {product1.price}")

# Try to set a negative price
product1.price = -500

# Delete price using deleter
del product1.price
