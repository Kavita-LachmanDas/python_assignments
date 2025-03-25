# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.





dictionaryy = {}

while True:
    
    number_input = input('enter a number... ')
    if number_input == "":
        break
    if number_input in dictionaryy:
        dictionaryy[number_input] += 1
    else:
        dictionaryy[number_input] = 1    


for number, count in dictionaryy.items():
    print(f"{number} appears {count} times.")