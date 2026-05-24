# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
list1=['scissor','paper','rock']

us=0
cs=0

n=int(input("Enter the number of rounds to be played:"))

for i in range(1,n+1):
    print("ROUND:",i)
    user=(input("Choose Rock, Paper or Scissor:")).lower()
    computer=random.choice(list1)
    print("Computer chose:", computer)

    if user==computer:
        print("Its a tie")
    elif user=='rock' and computer=='scissor':
        print("You won")
        us+=1
    elif user=='scissor' and computer=='paper':
        print("You won")
        us+=1
    elif user=='paper' and computer=='rock':
        print("You won")
        us+=1
    else:
         print("Computer won")
         cs+=1
    print("\t")
if us>cs:
    print("User won")
elif us<cs:
    print("Computer won")
else:
    print("Its a draw")

print("Final score:")
print("User:",us)
print("Computer:",cs)