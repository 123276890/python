# -*- coding: utf-8 -*-
# this is a guess the number game

import random

secretNumber = random.randint(1, 20)
print('i am thinking of a number between 1 and 20.')

# 6次机会
for guessTaken in range(1, 7):
    print('take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('your guess is too low')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break

if guess == secretNumber:
    print('Good job!')
else:
    print('Nope')