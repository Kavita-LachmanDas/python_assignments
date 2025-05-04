# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor)
#  and another message when it is destroyed (destructor).


class Logger:
    def __init__(self,msg):
        self.msg = msg 
        print(f"Constructor: {self.msg}")
    def __del__(self):
        print("Destructor: Object is being destroyed")

log = Logger("Logger object created")

del log