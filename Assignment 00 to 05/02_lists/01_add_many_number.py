l = []
def calculate__sum():
    while True : 
        userInput = int(input('write numbers.. '))
        l.append(userInput)
        summ = sum(l)
        if(userInput > 0):
            pass
        elif(userInput<=0):
            print(summ)
            break

calculate__sum()    