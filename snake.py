from turtle import *
class Snake:
    def __init__(self):
        self.t_objs = []
        for i in range(3):
            self.create_t_obj()
        self.t_objs[1].goto((-20), 0)
        self.t_objs[2].goto((-40), 0)
        self.current_heading = 0
        self.add_x=0
        self.add_y=0

    def create_t_obj(self):
        t = Turtle()
        t.shape('square')
        t.color('white')
        t.penup()
        self.t_objs.append(t)

    def attach(self):
        self.t_objs[len(self.t_objs)-1].goto(self.add_x,self.add_y)

    def move(self):
        self.add_x = self.t_objs[len(self.t_objs) - 1].xcor()
        self.add_y = self.t_objs[len(self.t_objs) - 1].ycor()
        for i in range(len(self.t_objs) - 1, 0, -1):
            self.t_objs[i].goto(self.t_objs[i - 1].xcor(), self.t_objs[i - 1].ycor())
        self.t_objs[0].forward(20)

    def up(self):
        if self.current_heading != 270:
            self.t_objs[0].setheading(90)
            self.current_heading=90

    def down(self):
        if self.current_heading != 90:
            self.t_objs[0].setheading(270)
            self.current_heading=270

    def right(self):
        if self.current_heading != 180:
            self.t_objs[0].setheading(0)
            self.current_heading=0

    def left(self):
        if self.current_heading != 0:
            self.t_objs[0].setheading(180)
            self.current_heading=180


