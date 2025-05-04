# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() 
# and __next__() to make the object iterable in a for-loop, counting down to 0.


class Countdown:
    def __init__(self, start):
        self.start = start  
        self.current = start  

    # __iter__ method to make the class iterable
    def __iter__(self):
        return self  # The instance itself is the iterator

    # __next__ method to return the next number in the countdown
    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # Stop when the countdown reaches 0
        else:
            self.current -= 1
            return self.current

# Create a Countdown object starting from 5
countdown = Countdown(5)

# Use the Countdown object in a for-loop (iterable behavior)
for number in countdown:
    print(number)
