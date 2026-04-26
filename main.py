from logic import *
from utils import *

while True:
    user = get_user_input()

    if user == "exit":
        print("Game exited!")
        break

    if user is None:
        continue

    comp = computer_choice()
    result = check_winner(user, comp)

    show_result(user, comp, result)

  