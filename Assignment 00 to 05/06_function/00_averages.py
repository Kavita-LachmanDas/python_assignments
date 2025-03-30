# Write a function that takes two numbers and finds the average between the two.
user1 = int(input('enter your first number .... '))
user2 = int(input('enter your second number .... '))  

def average(num1,num2):
  
    return (num1+num2)/2

av = average(user1,user2)
print(f"The average of {user1} and {user2} is {av}")