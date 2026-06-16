import random

choices = ["rock", "paper", "scissor"]

name = input("Enter your name: ")
print("Welcome to the game", name)

user = input("Enter your choice (rock, paper, scissor): ").lower()

if user not in choices:
    print("Invalid choice!")
else:
    computer = random.choice(choices) # Randomly select a choice for the computer

    print("Computer chose:", computer)

    if computer == user:
        print("It's a Tie!")

    # User wins
    elif (user == "rock" and computer == "scissor") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissor" and computer == "paper"):
        print("You Win!")

    # Computer wins
    else:
        print("Computer Wins!")
