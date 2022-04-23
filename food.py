from turtle import Turtle
from random import randint, uniform


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("navy")
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x = randint(-280, 280)
        y = randint(-280, 250)
        self.goto(x, y)
        self.shapesize(uniform(0.5, 2.0))
        self.color((randint(0, 255), randint(0, 255), randint(0, 255)))
