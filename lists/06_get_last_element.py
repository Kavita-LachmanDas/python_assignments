# Fill out the function get_last_element(lst)
#  which takes in a list lst as a parameter and prints the last element in the list.
#  The list is guaranteed to be non-empty, but there are no guarantees on its length.



def get_first_element(lst):
    print("last element:", lst[-1]) 


user_list = []

ninput = int(input("Enter number of elements: ")) 
for i in range(ninput):
    element = input(f"Enter element {i+1}: ")  
    user_list.append(element) 


get_first_element(user_list)