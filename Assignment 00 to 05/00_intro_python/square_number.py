# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0


def square():
    number = float(input('Type a number to see its square: '))
    print(f'{number} squared is {number*number:.1f}')

square()    