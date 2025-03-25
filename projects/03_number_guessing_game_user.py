import random

def computer_guess():
    low = 1
    high = 100

    attempts = 0
    while True:
        guess = random.randint(low, high)  
        attempts += 1
        feedback = input(f"Computer guessed {guess}. Is it too high (H), too low (L), or correct (C)? ")

        if feedback == "H":
            high = guess - 1 
        elif feedback == "L":
            low = guess + 1 
        elif feedback == "C":
            print(f"Yay! Computer guessed your number {guess} in {attempts} attempts.")
            break  


computer_guess()
