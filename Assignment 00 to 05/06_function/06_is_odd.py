# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd


def is_odd():
    for i in range(10,20):
        if(i % 2 == 0):
            print(i , 'Even', end=" ")
        else:
            print(i , 'Odd' , end=" ")

is_odd()            