import random

lower = int(0) 
upper = int(10) 

# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("You've only got one chance to guess the integer!\n")

# taking guessing number as input
guess = int(input("Guess a number:- ")) 

# Condition testing
if x == guess: 
    print("Congratulations you did it")
    
    

elif x > guess:
    print("You guessed too small!")
elif x < guess:
    print("You Guessed too high!")

print("\nYour guess was %d"%guess)
print("\nThe number is %d"%x)
print("Better Luck Next time!")

