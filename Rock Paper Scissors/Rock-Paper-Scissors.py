rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
moves = [rock, paper, scissors]
userinput = input("What's your move? Type 0 for rock, 1 for paper and 0 for scissors. \n")
userinputint = int(userinput)

if userinputint < 0 or userinputint > 2:
    print("You have typed an invalid number, you lose!")
else:
    print(moves[userinputint])

    cpuinput = random.randint(0,2)
    print (moves[cpuinput])

    if userinputint == cpuinput:
        print("It's a draw!")
    elif userinputint == 0 and cpuinput == 2:
        print("You Win!")
    elif userinputint == 1 and cpuinput == 0:
        print("You Win!")
    elif userinputint == 2 and cpuinput == 1:
        print("You Win!")
    else:
        print ("You Lose!")
   

 
