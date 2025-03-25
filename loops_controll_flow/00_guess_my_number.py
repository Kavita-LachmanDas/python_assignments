# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48


import random
generate = random.randint(1,99)
while True:
    user_guess = int(input('enter a number between 1 to 99 .... '))
    
    if(user_guess > generate):
        print('your guess is too high....')
    elif(user_guess < generate):
        print('your guess is too low....' ) 
    elif(user_guess==generate):
        print(f"Congrats! The number was: {generate}")    
        break
    else:
        print('faileddddd.. try again..')       