
import random as rm
print("Welcome to Rock/Paper/Scissor Game :)")
Name = input("Enter Your Name: ")

user_wins = 0
computer_wins = 0
options = ["rock","paper","scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_Number = rm.randint(0,2)
    # The  index number is Rock is 0,Paper is 1, Scissor is 2.
    computer_pick = options[random_Number]
    print("Computer Pick "+computer_pick+".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You Won ")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won ")
        user_wins += 1

    elif user_input == "scissor" and computer_pick == "paper":
        print("You Won ")
        user_wins += 1
    else:
        print("You Lost :( ")
        computer_wins +=1

print(Name+" You Won",user_wins,"times.")
print("Computer Won",computer_wins,"times.")
print("Thank You for Coming.")