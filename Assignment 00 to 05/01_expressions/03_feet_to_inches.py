# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. 
# Foot is the singular, and feet is the plural.



def inches():
    user = float(input('Enter number of feet: '))
    convert = user * 12
    unit = "foot" if user == 1 else "feet"
    print(f"{user} {unit} is {convert} inches.")

    

inches()    