# Task 1 - call capitalize_names() function for testing
# Task 2 - call camel_to_snake() function for testing
# Task 3 - call function programming_dict() for testing
# Task 4 - call function print_names() for testing
# Task 5 - call function print_int() for testing
# Task 6 - call function symbol_counter() for testing
# Task 7 - call function updated_calculator() for testing

import sys


def capitalize_names():
    names_list = ["john", "marta", "james", "amanda", "marianna"]
    capitalized_list = [name.capitalize() for name in names_list]
    print(capitalized_list)


def camel_to_snake():
    camel_case = ["FirstItem", "FriendsList", "MyTuple"]
    snake_case = []
    for camel_case_var in camel_case:
        snake_case_var = ''.join(['_' + i.lower() if i.isupper() else i for i in camel_case_var]).lstrip('_')
        snake_case.append(snake_case_var)
    print(snake_case)


def programming_dict():
    pl_dict = {
        "Java": "James Gosling",
        "Python": "Guido van Rossum",
        "Ruby": "Yukihiro Matsumoto",
        "C": "Dennis Ritchie"
    }

    for language, developer in pl_dict.items():
        print(f"My favorite programming language is {language}. It was created by {developer}.")
    del pl_dict["Ruby"]
    print(pl_dict)


def print_names():
    names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
    for x in names:
        if type(x) is str:
            print(x)
        else:
            continue


def print_int():
    types = [1, 1000, 2, 12, {'key': 'value'}]
    for x in types:
        if type(x) is int:
            print(x)
        else:
            print(f"This loop is not working with {type(x)} data type")
            break


def symbol_counter():
    user_input = input("Please enter you text: ")
    symbol_dict = {}
    for x in user_input:
        symbol_dict[x] = user_input.count(x)
    result = [f"{key},{value}" for key, value in symbol_dict.items()]
    print(" ".join(result))


def updated_calculator():
    tries_left = 2

    def get_user_input():
        nonlocal tries_left
        if tries_left <= 0:
            print("You have no more tries left.")
            sys.exit()

        try:
            num1 = float(input("Please enter the first number: "))
        except ValueError:
            tries_left -= 1
            print(f"Invalid input. Tries left {tries_left}")
            return get_user_input()

        operation = input("Please select the operation (+, -, *, /): ")
        if operation not in ["+", "-", "*", "/"]:
            tries_left -= 1
            print(f"Invalid input. Tries left {tries_left}")
            return get_user_input()

        try:
            num2 = float(input("Please enter the second number: "))
        except ValueError:
            tries_left -= 1
            print(f"Invalid input. Tries left {tries_left}")
            return get_user_input()
        if operation == "/" and num2 == 0:
            tries_left -= 1
            print(f"Division by zero is not allowed. Tries left {tries_left}")
            return get_user_input()

        return num1, operation, num2

    num1, operation, num2 = get_user_input()
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        print(num1 / num2)

