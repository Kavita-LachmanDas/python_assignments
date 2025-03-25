import random
def start_game():
   
    computer_choice = random.choice(['rock','paper','scissor'])
    print(computer_choice)
    while True:
        user_choice = input("select one 'Rock , Paper , Scissor'  ")
        if user_choice== computer_choice:
            print("It's a tie!")
            break
        elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
            print("user win! 🎉")
            break
        else:
            print("Computer wins! 😢")
            break
start_game()

