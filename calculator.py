def add():
    result = user_input_1 + user_input_2
    print(result)


def substract():
    result = user_input_1 - user_input_2
    print(result)


def multiply():
    result = user_input_1 * user_input_2
    print(result)


def divide():
    result = user_input_1 / user_input_2
    print(result)


while True:
    chosen_action = input(
        "Welcome to calculator :) Choose your action: +,-,*,/ ")

    user_input_1 = int(input("Enter the first number:"))
    user_input_2 = int(input("Enter the second number:"))

    if chosen_action == "+":
        add()
    elif chosen_action == "-":
        substract()
    elif chosen_action == "*":
        multiply()
    elif chosen_action == "/":
        divide()
