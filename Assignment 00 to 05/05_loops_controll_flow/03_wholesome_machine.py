# Write a program which prompts the user to type an affirmation of your choice 
# (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!

# Here's a sample run of the program (user input is in blue):

# Please type the following affirmation: I am capable of doing anything I put my mind to.
#  Hmmm That was not the affirmation. Please type the following affirmation: 
# I am capable of doing anything I put my mind to. I am capable of doing anything I put my mind to. That's right! :)

# Note that you can call input() with no prompt and it will still wait for a user to type something!


_affirmative = "I am capable of doing anything I put my mind to."

while True:
    user = input(f"Please type the following affirmation: {_affirmative} \t \n ")
    if(user == " "):
        print('write somethingg  ')
    if(user == _affirmative):
        print("That's right! ")
        break
    
    elif(user != _affirmative):
        print('thats wrong plz write again!!!!!!!  ')       