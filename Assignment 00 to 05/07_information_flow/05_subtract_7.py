# Fill out the subtract_seven helper function to subtract 7 from num, 
# and fill out the main() method to call the subtract_seven helper function! If you're stuck, 
# revisit the add_five example from lecture.



def subtract_seven(num):
    sub = num - 7
    return sub

def main():
    num = int(input('enter your number.: '))
    gett = subtract_seven(num)
    print(gett)
main()
