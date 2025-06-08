from turtle import *
import random
class Food:
    def __init__(self):
        self.f= Turtle()
        self.f.penup()
        self.f.color("red")
        self.f.shape("circle")
        self.f.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.tp()
    def tp(self):
        self.f.goto(random.randint(-280,280), random.randint(-280,280))