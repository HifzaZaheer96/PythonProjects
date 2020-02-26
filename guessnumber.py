#!/usr/bin/env python3.8

import random

# global variable
player_guesses_Taken = 0

print('Hello! What is your name?')
name = input()

number = random.randint(1, 20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')

while player_guesses_Taken < 6:
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    player_guesses_Taken +=1

    if guess < number:
        print('Sorry,Your guess is too low.') # There are eight spaces in front of print.

    if guess > number:
        print('Sorry,Your guess is too high.')

    if guess == number:
        break

if guess == number:
    player_guesses_Taken = str(player_guesses_Taken)
    print('Good job, ' + name + '! You guessed my number in ' + player_guesses_Taken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)