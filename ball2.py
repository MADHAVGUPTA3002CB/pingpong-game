from turtle import Turtle
import random

class Ball2(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.xmove=random.randint(5,15)
        self.ymove=random.randint(5,15)
    def move(self):
        newx=self.xcor()+self.xmove
        newy=self.ycor()+self.ymove
        self.goto(newx,newy)

    def bounce(self):
        self.ymove*=-1

    def colliwthpdl(self):
        self.xmove*=-1

    def resetpos(self):
        self.goto(0,0)
        self.xmove*=-1