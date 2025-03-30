
print("\n \n \t \t  --------------Welcome to the Guess the Number Game!-----------\n")


import random
def guessing_game():
    generate = random.randint(1,100)
    attempts = 0
    while True:
        userGuess = int(input('I have chosen a number between 1 and 100. \n enter your guess between 1 to 100.....  '))
        attempts += 1
        if(userGuess > generate):
            print('your number is too high')
        elif(userGuess < generate):
            print('your guess is too low')
        elif(userGuess == generate):
            print(f"\n \t you guessed correct number congratss \n your guess {userGuess} and computer guess {generate} \n \t 🎉 You guessed the correct number in {attempts} attempts! Wohooo!! 🎉")        
            break
        else:
            print("try againnnn")

guessing_game()