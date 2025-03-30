# Fill out the double(num) function to return the result
#  of multiplying num by 2. We've written a main() function 
# for you which asks the user for a number, calls your code for double(num) ,
#  and prints the result.

# Here's a sample run of the program (user input in bold italics):

# Enter a number: 2 Double that is 4

def double(num):
    return num * 2

def main():
    user = int(input('enter your number... '))
    p = double(user)
    print(f"Double that is {p}")

main()