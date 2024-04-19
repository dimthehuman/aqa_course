# Task 1 - call is_palindrome() function for testing
# Task 2 - call word_in_text() function for testing
# Task 3 - call email_validator() function for testing
# Task 4 - call print_last_three() function for testing


def is_palindrome():
    word = input("Please enter your word: ")
    if word.lower() == word[::-1].lower():
        print("+")
    else:
        print("-")


def word_in_text():
    text = input("Please enter your text: ")
    word = input("Please enter your word: ")
    if word.lower() in text.lower():
        print("YES")
    else:
        print("NO")


def email_validator():
    email = input("Please enter your email: ")
    if "." in email.lower() and "@" in email.lower():
        print("YES")
    else:
        print("NO")


def print_last_three():
    text = input("Please enter your text with spaces: ")
    if len(text.split()) < 3:
        print(f"Your text has {len(text.split())} elements. Required three or more.")
    else:
        print(text.split()[-3:])


