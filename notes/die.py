"""
what does a die have?
-sides
- values

what can it do?
- Roll
- get values


"""
import random


class Die:
    def __init__(self, num_sides):
        self.sides = num_sides
        self.value = 1

    def get_value(self):
        return self.value

    def roll(self):
        self.value = random.randint(1, self.sides)

