import random

def computer_choice():
    return random.choice(["stone", "paper", "scissors"])

def check_winner(user, comp):
    if user == comp:
        return "Draw"
    elif (user == "stone" and comp == "scissors") or \
         (user == "paper" and comp == "stone") or \
         (user == "scissors" and comp == "paper"):
        return "You Win"
    else:
        return "You Lose"