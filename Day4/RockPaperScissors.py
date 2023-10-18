import random
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
print("Welcome to Rock Paper Scissors gambe by Akuya!")
user = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0,2)
signs = [rock,paper,scissors]
msg = ""
if user <= 2 and user >= 0:
    if user - computer == -2:
        msg ="You win!"
    elif user > computer:
        msg = "You win!"
    elif user == computer :
        msg = "It's a draw"
    else:
        msg = "You lose"

    print(f"You chose:\n{signs[user]}")
    print(f"Computer chose:\n{signs[computer]}")
    print(f"Results:\n{msg}")
else:
    print("Invalid input. You lose!")
