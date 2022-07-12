from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,xcord):
        super().__init__()
        self.shape("square")

        self.color("white")
        self.shapesize(5,1,1)
        self.penup()
        self.goto(xcord,0)
        print(xcord)
        print(self.pos())

    def moveup(self):

        y=self.ycor()+20
        xcord=self.xcor()
        self.goto(xcord,y)
    def movedown(self):
        y=self.ycor()-20
        xcord=self.xcor()
        self.goto(xcord,y)
    