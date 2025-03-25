# In this program we show an example of using dictionaries to keep track of information in a phonebook.





phonebook = {}

while True:
    name = input("Enter name (press enter to stop): ")
    
 
    if name == "":
        break

    number = input("Enter phone number: ")

  
    phonebook[name] = number 

# Print all contacts
print("\n📖 Your Phonebook:")
for name, number in phonebook.items():
    print(f"{name}: {number}")
