# Simulate rolling two dice, and prints results of each roll as well as the total.


import random

generate1 = random.randint(1, 6)
generate2 = random.randint(1, 6)
total = generate1 + generate2

print(f"First die: {generate1}")
print(f"Second die: {generate2}")
print(f"Total: {total}")
