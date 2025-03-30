# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

# Here is an example run of the program (user input is in bold italics):

# How many (apple) do you want?: 2

# How many (durian) do you want?: 0

# How many (jackfruit) do you want?: 1

# How many (kiwi) do you want?: 0

# How many (rambutan) do you want?: 1

# How many (mango) do you want?: 3

# Your total is $99.5


fruit_prices = {
    "apple": 5.0,   
    "durian": 15.0,   
    "jackfruit": 12.5,  
    "kiwi": 7.0,  
    "rambutan": 8.0,  
    "mango": 6.5
}
total_cost = 0
quantity = []

for i in fruit_prices:
    user = int(input("How many (" + i + ") do you want to buy?: "))
    gh = fruit_prices.values()
    quantity.append(user)
  
    p = fruit_prices[i]*user
    total_cost = total_cost + p
    # print(total_cost)
    
print(f"\nYour total cost is: ${total_cost}")