
print("\n \t \t \t---------------- Welcome to Mad Libs!----------------")



def mad_libs():
    
    noun = input('Enter Noun ')
    verb = input('Enter Verb ')
    adj = input('Enter Adjective')
    story = f"One fine morning, a {adj} {noun} woke up and decided to {verb} all day long."
    print(story)

mad_libs()    
