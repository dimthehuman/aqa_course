# Task 1 - call convert_celsius() function for testing
# Task 2 - call mix_parameters() function for testing
# Task 3 - call calculator() function for testing

def convert_celsius():
    celsius = float(input("Please enter degrees in Celsius: "))
    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15
    print(f"Temperature in Fahrenheit: {fahrenheit}\nTemperature in Kelvins: {kelvin}")


def mix_parameters():
    v1 = float(input("Please enter the first volume: "))
    t1 = float(input("Please enter the first temperature: "))
    v2 = float(input("Please enter the second volume: "))
    t2 = float(input("Please enter the second temperature: "))
    mix_volume = v1 + v2
    mix_temp = (v1 * t1 + v2 * t2) / mix_volume
    print(f"Volume: {mix_volume}.\nTemperature: {mix_temp}")


def calculator():
    num1 = float(input("Please enter the first number: "))
    operation = input("Please select the operation (+, -, *, /): ")
    num2 = float(input("Please enter the second number: "))
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
            print("Division by zero is not allowed")
    else:
        print("Unknown operation")
