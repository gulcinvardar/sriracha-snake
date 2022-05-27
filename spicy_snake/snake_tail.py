from turtle import position
from spicy_snake.moves import move
from spicy_snake.playground import Playground


class Snake:

    def __init__(self, xstart, ystart):
        self.head = xstart, ystart
        self.tail = [self.head]
        self.growing = 0
        self.direction = 'right'


    def grow(self):
        """Memorizes that the snake should grow when it moves next time"""
        self.growing += 1


    def forward(self):
        """Moves the snake one step ahead"""
        self.head = move(self.head, self.direction)
        self.tail.append(self.head)
        if self.growing == 0:
            self.tail.remove(self.tail[0])
        else: 
            self.growing -= 1


    def set_direction(self, direction):
        """Moves the head to a new direction"""
        self.direction = direction


    def eat(self, playground):
        """Eats food at the position of the head, if any"""
        if self.head == playground.food:
            playground.food = None
            self.grow()


    def check_collision(self, playground):
        """Returns True if the head hits an obstacle or the tail"""
        if playground.is_obstacle(position=self.head):
            return True
        else:
            return self.head in self.tail[:-1]


         