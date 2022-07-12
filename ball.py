
from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.ang=random.randint(40,89)
        self.left(self.ang)
        self.speed(3)
        self.movefd()
        
    def movefd(self):
        while self.xcor()<335  and self.ycor()<290:
            self.forward(10)
        self.changedirection()
    def changedirection(self):
        if self.xcor()>=320  or self.ycor()>=280 or self.xcor()<=-320 or self.ycor()<=-280:
            if self.ang<0:
                self.left(2*self.ang)
            else:
                self.right(2*self.ang)
            self.forward(20)
            self.movefd()