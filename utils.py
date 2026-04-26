def get_user_input():
    user = input("Enter stone / paper / scissors (or type 'exit'): ").lower()

    if user == "exit":
        return "exit"

    if user not in ["stone", "paper", "scissors"]:
        print("Invalid input!")
        return None

    return user


def show_result(user, comp, result):
    print("You:", user)
    print("Computer:", comp)
    print("Result:", result)