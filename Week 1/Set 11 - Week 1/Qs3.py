# 3: Write a python program where the program takes a random integer between 1 to 10, the
# user is then prompted to input a guess number. If the user input matches with guess number,
# the program will display a message &quot;Good Work&quot; otherwise display a message &quot;Not
# matched&quot;.

import random
i = 1
print("Press q to exit from the loop")
for i in range(1000):
    comp = random.randint(0,11)
    guess = input("Enter a random number: ")
    if guess == 'q':
        break
    print("Computer's Guess: ", comp)
    if int(guess) == comp:
        print("Good Work")
    else:
        print("Not matched")
