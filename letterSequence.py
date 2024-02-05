#Remember sequence of letters

import random

def generateSequence(length):
    lettersList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(lettersList) for _ in range(length))

def displaySequence(sequence):
    print("Generated sequence: ",end="")
    for i in range(len(sequence)):
        print(sequence[i], end="")
        if i % 2 == 1:
            print(" ", end="")

def checkSequence(userInput, sequence):
    if userInput.upper() == sequence:
        print(f'You\'re right! | Sequence: {sequence}  | Your guess: {userInput}')
    else:
        print(f'Wrong! | Sequence: {sequence} | Your guess: {userInput}')

#Main program
SEQUENCE_LENGHT = 8
finalSequence = generateSequence(SEQUENCE_LENGHT)

displaySequence(finalSequence)

input("\nPress enter when you are ready")
print(100 * '\n')

userSequence = input("Enter your guess: ")
checkSequence(userSequence, finalSequence)
