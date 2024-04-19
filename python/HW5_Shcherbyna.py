# Task 1 - call square_root() function for testing
# Task 2 - call square_root_with_VE() function for testing
# Task 3 - call calc() function for testing

import math


def square_root():
    class CustomNegativeNumberError(Exception):
        def __init__(self, message="Custom Error Message"):
            self.message = message
            super().__init__(self.message)

    try:
        num = int(input("Enter you number: "))
        if num < 0:
            raise CustomNegativeNumberError()
    except CustomNegativeNumberError:
        print("Number shouldn't be negative.")
    else:
        print(math.sqrt(num))
    finally:
        print("Calculation complete.")


def square_root_with_ve():
    class CustomNegativeNumberError(Exception):
        def __init__(self, message="Custom Error Message"):
            self.message = message
            super().__init__(self.message)

    try:
        num = int(input("Enter you number: "))
        if num < 0:
            raise CustomNegativeNumberError()
    except CustomNegativeNumberError:
        print("Number shouldn't be negative.")
    except ValueError:
        print("Invalid input.")
    else:
        print(math.sqrt(num))
    finally:
        print("Calculation complete.")


def calc():
    is_on = True

    while is_on:
        try:
            num1 = float(input("Please enter the first number: "))
            operation = input("Please select the operation (+, -, *, /): ")
            if operation not in ["+", "-", "*", "/"]:
                raise ValueError
            num2 = float(input("Please enter the second number: "))
        except ValueError:
            retry = input(f"Invalid input. Retry? (y/n): ")
            if retry.lower() != "y":
                is_on = False
            else:
                continue
        else:
            if operation == "+":
                print(num1 + num2)
            elif operation == "-":
                print(num1 - num2)
            elif operation == "*":
                print(num1 * num2)
            elif operation == "/":
                try:
                    print(num1 / num2)
                except ZeroDivisionError:
                    retry = input("Division by zero is not allowed. Retry? (y/n):  ")
                    if retry.lower() != "y":
                        is_on = False
                    else:
                        continue

        print("Calculation complete.")

        restart = input("Do you want to restart the calculator? (y/n): ")
        if restart.lower() == "y":
            continue
        else:
            is_on = False
            print("Exiting the calculator.")

