from random import randint


class Die:
    """A single die"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        """Return a random number based upon the sides of the die"""

        return randint(1, self.sides)
