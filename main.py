# This game is made by Kingson
# Game written in python that guesses your number

import random
import time

print("Welcome to the guessing game. I will be choosing a number between 1 and 100.")
time.sleep(2)
print("Picking a number...")

correct_number = random.randint(1,100)
time.sleep(2)

guess = int(input("What is your guess?: "))
guess_count = 1

while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
        guess = int(input("Try again. You need to guess higher. What is your guess?: "))
    else:
        guess = int(input("Try again. You need to guess lower. What is your guess?: "))

print(f"Congrats! The right answer is {correct_number}. It took you {guess_count} guesses.")