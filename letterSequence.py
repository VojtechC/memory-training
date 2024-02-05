#Remember sequence of letters

import random

SEQUENCE_LENGTH = 8
lettersList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Z']

finalSequence = ""
for _ in range(SEQUENCE_LENGTH):
  finalSequence += random.choice(lettersList)

def displaySequence(sequence):
  for i in range(SEQUENCE_LENGTH):
    print(sequence[i],end="")
    if i % 2 == 1:
      print(" ",end="")
  
  
def checkSequence(sequence):
  userSequence = input().upper()
  if userSequence == sequence:
    print(f'You\'re right! | Sequence: {sequence}  | Your guess: {userSequence}')
  else:
    print(f'Wrong! | Sequence: {sequence} | Your guess: {userSequence}')
   
  
displaySequence(finalSequence)

input("Press enter when you are ready")
print(100*'\n')

checkSequence(finalSequence)
