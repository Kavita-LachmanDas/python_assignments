# Simulate rolling two dice, three times. Prints the results of each die roll.
# This program is used to show how variable scope works.

import random

for i in range(1, 4):
    die1 = random.randint(1, 6) 
    die2 = random.randint(1, 6)  
    print(f"Roll number {i}: Die 1 = {die1}, Die 2 = {die2}")
