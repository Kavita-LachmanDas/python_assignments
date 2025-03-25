
import time
import pyttsx3  # Text-to-Speech module

engine = pyttsx3.init()  # Initialize voice engine

timer = int(input("Enter seconds to start the countdown: "))

for i in range(timer, 0, -1):
    print(i)
    time.sleep(1)

print("Time's Up!")  
engine.say("Time's Up!")  # Voice output
engine.runAndWait()  # Wait for speech to complete
