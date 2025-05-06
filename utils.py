import random

# Constants for roulette wheel
RED_NUMBERS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
BLACK_NUMBERS = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}

# Define roulette numbers (0 is green)
ROULETTE_WHEEL = list(range(37))  # 0 to 36 (including the green 0)

def spin_wheel():
    """Simulate a roulette spin and return a number between 0 and 36."""
    return random.choice(ROULETTE_WHEEL)

def get_color(number):
    """Return the color of the roulette number (red, black, or green)."""
    if number == 0:
        return 'green'
    elif number in RED_NUMBERS:
        return 'red'
    elif number in BLACK_NUMBERS:
        return 'black'
    else:
        return 'unknown'

def is_even(number):
    """Check if the number is even (ignoring 0 for even/odd)."""
    return number != 0 and number % 2 == 0

def is_odd(number):
    """Check if the number is odd."""
    return number != 0 and number % 2 != 0

def is_in_dozen(number, dozen):
    """Check if the number is in the given dozen (1-12, 13-24, or 25-36)."""
    if dozen == 1:
        return 1 <= number <= 12
    elif dozen == 2:
        return 13 <= number <= 24
    elif dozen == 3:
        return 25 <= number <= 36
    return False

def is_in_column(number, column):
    """Check if the number is in the selected column (1st, 2nd, or 3rd)."""
    column_mapping = {
        1: [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
        2: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
        3: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
    }
    return number in column_mapping[column]

