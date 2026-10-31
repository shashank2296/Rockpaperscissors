rock = '''
    _______
---'   ____)
      (_)
      (_)
      ()
---.(_)
'''

paper = '''
    _______
---'   ___)___
          ______)
          _______)
         _______)
---.)
'''

scissor = '''
    _______
---'   ___)___
          ______)
       __________)
      ()
---.(_)
'''

import random
human_choice=input("Enter your choice 'rock' 'paper' or 'scissor'")
RandomNum=random.randint(0,2)
Set=["rock","paper","scissor"]
Comp=Set[RandomNum]
if human_choice=="rock" and Comp=="paper":
    print(rock)
    print(paper)
    print("You lost")
elif human_choice=="paper" and Comp=="rock":

    print(paper)
    print(rock)

    print("You Won")
elif human_choice=="scissor" and Comp=="rock":
    print(scissor)
    print(rock)
    print("You lost")

elif human_choice=="rock" and Comp=="scissor":
    print(rock)
    print(scissor)
    print("You Won")
elif human_choice=="paper" and Comp=="scissor":
    print(paper)
    print(scissor)
    print("You lost")
elif human_choice == "scissor"and Comp == "paper":
    print(scissor)
    print(paper)
    print("You Won")
elif human_choice == "paper"and Comp == "paper":
    print(paper)
    print(paper)
    print("tie")
elif human_choice == "rock" and Comp == "rock":
    print(rock)
    print(rock)
    print("tie")
elif human_choice == "scissor"and Comp == "scissor":
    print(scissor)
    print(scissor)
    print("tie")
