# Fill out the function shorten(lst) which removes elements 
# from the end of lst, which is a list, and prints each item
#  it removes until lst is MAX_LENGTH items long. If lst is 
# already shorter than MAX_LENGTH you should leave it unchanged. 
# We've written a main() function for you which gets a list and passes
#  it into your function once you run the program. For the autograder to pass
#  you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

max_len = 3 

def shortend(lst):
    while True:
        elem = input("Please enter an element of the list or press enter to stop: ")

        if elem == "": 
            break
        
        lst.append(elem)  
        
        if len(lst) > max_len:  
            removed = lst.pop()  
            print("Removed:", removed)

    print("Final List:", lst)  


my_list = []
shortend(my_list)
