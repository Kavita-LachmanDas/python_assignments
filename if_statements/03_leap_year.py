
def checking_leap_year():
    user = int(input('Enter a year... '))

    if user % 400 == 0:  
        print("That's a leap year!")  
    elif user % 100 == 0:  
        print("That's not a leap year.")  
    elif user % 4 == 0:  
        print("That's a leap year!")  
    else:  
        print("That's not a leap year.")  

checking_leap_year()


