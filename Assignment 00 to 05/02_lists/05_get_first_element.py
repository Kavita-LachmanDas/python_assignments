# Fill out the function get_first_element(lst) 
# which takes in a list lst as a parameter and prints
#  the first element in the list. The list is guaranteed to be non-empty. We've written 
# some code for you which prompts the user to input the list one element at a time.


def get_first_element(lst):
    print("First element:", lst[0]) 


user_list = []

ninput = int(input("Enter number of elements: ")) 
for i in range(ninput):
    element = input(f"Enter element {i+1}: ")  
    user_list.append(element) 


get_first_element(user_list)
