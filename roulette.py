import random

class Roulette:
    def spin(self):
        number = random.randint(0, 36)
        color = 'green' if number == 0 else 'red' if number % 2 == 0 else 'black'
        return number, color

    def is_win(self, bet_type, result):
        number, color = result
        if bet_type == "red":
            return color == "red"
        elif bet_type == "black":
            return color == "black"
        else:
            return False

