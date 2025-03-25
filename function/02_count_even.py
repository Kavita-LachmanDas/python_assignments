# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.

# If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!

def get_numbers():
   
    numbers = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":  
            break
        try:
            numbers.append(int(user_input)) 
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return numbers

def count_even(lst):
    """Counts and prints the number of even numbers in a list."""
    even_count = sum(1 for num in lst if num % 2 == 0)
    print(f"Total even numbers: {even_count}")


numbers_list = get_numbers() 
count_even(numbers_list)  

