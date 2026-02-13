import random
import time

def stone_paper_scissor():
    print("Welcome to Stone Paper Scissor Game\n")

    print("Rules:")
    print("Stone breaks Scissor")
    print("Paper covers Stone")
    print("Scissor cuts Paper\n")

    choices = ["stone", "paper", "scissor"]

    user = input("Choose Stone, Paper or Scissor: ").lower()

    if user not in choices:
        print("Invalid choice. Please choose correctly.")
        return

    print("\nComputer is thinking", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
    print()

    computer = random.choice(choices)

    print("\nYou chose:", user.capitalize())
    print("Computer chose:", computer.capitalize())

    if user == computer:
        print("Result: Draw")

    elif (user == "stone" and computer == "scissor") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissor" and computer == "paper"):
        print("Result: You Win")

    else:
        print("Result: Computer Wins")

    print("\nThanks for playing")


stone_paper_scissor()
