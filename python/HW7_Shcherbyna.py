"""
# Task 1 - call custom_map and custom_filter functions. Example: custom_filter(lambda x: x%2 == 0, [1, 2, 3, 4, 5, 6])
# Task 2 - call lambda_power function. Example of using:
power = lambda_power(2)
result = power(3)
print(result)
# Task 3 - call eval_func function
"""


def custom_map(func, iterable):
    final = []
    for x in iterable:
        final.append(func(x))
    print(final)


def custom_filter(func, iterable):
    final = []
    for x in iterable:
        if func(x):
            final.append(x)
    print(final)


def lambda_power(x):
    return lambda y: x ** y


def eval_func():
    text_func = input("Please enter your function: ")
    try:
        result = eval(text_func)
    except NameError:
        print("Unknown function")
    else:
        if result is not None:
            print(result)
