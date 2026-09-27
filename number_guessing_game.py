# Number guessing game

import random
n=random.randint(1,100)
print("Guess any number between 1 to 100")
while True:
    g=int(input("Enter your guess:-"))
    if g==n:
        print("Correct.!!, You guessed the number.")
        break
    elif g<n:
         print("Too low.!, Try again.")
    else:
        print("Too high.!, Try again.")

