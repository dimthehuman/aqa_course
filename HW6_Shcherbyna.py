# Task 1 - call sum_range() function for testing
# Task 2 - call square() function for testing
# Task 3 - call process_user_input() function and pass get_user_input() as parameter for testing

def sum_range(start, end):
    if start > end:
        start, end = end, start
    total = sum(range(start, end + 1))
    print(total)


def square(side):
    perimeter = side * 4
    area = side**2
    diagonal = round(side * 2**0.5, 2)
    print(f"Perimeter: {perimeter}. Area: {area}. Diagonal: {diagonal}.")


def get_user_input():
    user_input = input("Please enter the data: ")
    return user_input


def process_user_input(data):
    data_type = None
    try:
        if isinstance(eval(data), dict):
            data_type = dict
        elif isinstance(eval(data), list):
            data_type = list
        elif isinstance(eval(data), int):
            data_type = int
        elif isinstance(eval(data), tuple):
            data_type = tuple
    except NameError:
        print("Unknown data type.")
    else:
        print(f"User is going to work with {data_type}")




