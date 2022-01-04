import random
from turtle import Turtle
import time
STARTING_HEADING = [20, 30, 40, 50, 60, 70, 110, 120, 130, 140, 150, 160, 210, 220, 230, 240, 250,
                    300, 310, 320, 330, 340]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(1)
        self.color('white')
        self.penup()

    def move(self):
        self.forward(4)

    def start_ball(self):
        self.setposition(0, 0)
        self.setheading(random.choice(STARTING_HEADING))

    def wall_bounce(self):
        self.setheading(360 - self.heading())

    def paddle_bounce(self):
        self.setheading(540 - self.heading())