# Number guessing game

This is a simple program that helps generate a simple number generator game

# Features
1. Randomly generates a number between 1 and 100
2. Gives feedback if the guess is too high or too low 
3. Keeps asking until the correct number is guessed

# Prerequisite
--> Python 3.x should be installed on your system

# Setup

1. Clone this repository:
```bash 
git clone https://github.com/Neer06/NeerDesai.git
```
2. Navigate into the project folder
``` bash 
cd NeerDesai
```

# Dependencies
no external dependencies or libraries are required- the project only uses python's built-in 'random','input()',and 'print()' functions.


# How to run

```bash
python number_guessing_game.py
```

# Usage
1. When the program starts , it picks a random number between 1 and 100 
2. You will see:
	" Guess any number between 1 and 100 "
	" Enter your guess"
3. Enter a number and press enter 
4. The program tells you if your guess is too low high,or correct
5. Keep guessing until you find the number


# Example

Guess any number between 1 to 100
Enter your guess: 50
Too high.!, Try again.
Enter your guess: 25
Too low.!, Try again.
Enter your guess: 37
Correct.!!, You guessed the number

# Notes 

The number to guess is randomly generated each time you run the program , so it will differ every run
