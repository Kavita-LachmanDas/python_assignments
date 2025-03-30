def get_element(items, pos):
    """Returns the element at the specified index or an error message."""
    if 0 <= pos < len(items):
        return items[pos]
    return "Index out of range."

def update_element(items, pos, new_val):
    """Modifies the element at the specified index if valid."""
    if 0 <= pos < len(items):
        items[pos] = new_val
        return "Value updated successfully."
    return "Index out of range."

def extract_slice(items, start_pos, end_pos):
    """Returns a sliced list based on the given range."""
    return items[start_pos:end_pos] if 0 <= start_pos < len(items) and 0 <= end_pos <= len(items) else "Invalid index range."

def list_game():
    """Simple text-based game to interact with a list."""
    data = ["apple", "banana", "cherry", "date", "elderberry"]
    
    while True:
        print("\nCurrent list:", data)
        print("Choose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        user_choice = input("Enter your choice (1-4): ")
        
        if user_choice == "1":
            pos = int(input("Enter the index to access: "))
            print("Element:", get_element(data, pos))
        
        elif user_choice == "2":
            pos = int(input("Enter the index to modify: "))
            new_val = input("Enter the new value: ")
            print(update_element(data, pos, new_val))
        
        elif user_choice == "3":
            start_pos = int(input("Enter the start index: "))
            end_pos = int(input("Enter the end index: "))
            print("Sliced list:", extract_slice(data, start_pos, end_pos))
        
        elif user_choice == "4":
            print("Exiting the game.")
            break
        
        else:
            print("Invalid choice. Try again.")

# Run the game
list_game()
