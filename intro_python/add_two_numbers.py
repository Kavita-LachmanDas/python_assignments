# Write a Python program that takes two integer inputs
#  from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.



def summ():
    number1 = int(input('Enter Your First Number... '))
    number2 = int(input('Enter Your Second Number... '))
    total = number1 + number2
    print(f"Sum Of {number1} and {number2} is {total}")

summ()    