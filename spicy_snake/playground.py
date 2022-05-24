import random
from turtle import position

class Playground:
    """Manages the plaground"""

    def __init__(self, xsize, ysize):
        self.xsize = xsize
        self.ysize = ysize
        self.food = None

    @property 
    def size(self):
        return self.xsize, self.ysize

    def is_obstacle(self, position):
        x, y = position
        if (
            0 < x < self.xsize and
            0 < y < self.ysize
        ):
            return False
        return True


    def add_food(self, position):
        if self.is_obstacle(position):
          self.food = position
        else:
            self.food = None

    def add_random_food(self):
        x = random.randint(1, self.xsize -1)
        y = random.randint(1, self.ysize -1)
        if not self.is_obstacle(position):
            self.add_food(position)