import random

## part1
choices = ["stone","paper","scissors"]
botchoices = random.choice(choices)
userchoices = input("enter stone/paper/scissors: ")

## part2
print("Computer:", botchoices)
print("You:", userchoices)

if userchoices == botchoices:
    print("eqaul")

elif  (userchoices == "stone" and botchoices == "scissors") or \
     (userchoices == "paper" and botchoices == "stone") or \
     (userchoices == "scissors" and botchoices == "paper"):
    print("You win!")
else:
    print("Computer wins!")    


