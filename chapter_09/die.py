from random import randint


class Die():
    """a simple attempt to model dice"""

    def __init__(self, sides=6):
        """initilize a die"""
        self.sides = sides

    def roll_die(self):
        roll = randint(1, self.sides)
        print(f"You rolled a: {roll}")
