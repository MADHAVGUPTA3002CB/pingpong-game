from turtle import Turtle,Screen
from paddle import Paddle
from ball2 import Ball2
from scoreboard import ScoreBoard
import time
scoreboard=ScoreBoard()
screen=Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("SADDA PONG GAME")

l_paddle=Paddle(-350)
r_paddle=Paddle(350)
print(r_paddle.color())

screen.listen()
screen.onkey(l_paddle.moveup,"w")
screen.onkey(l_paddle.movedown,"s")
screen.onkey(r_paddle.moveup,"Up")
screen.onkey(r_paddle.movedown,"Down")

ball = Ball2()
game_ison=True
t=0.1
while game_ison:
    time.sleep(t)
    if t>0.03:
        t-=0.00001
    screen.update()
    ball.move()
    #detect collision with wwall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    #detect collision wwith paddle
    if (ball.xcor()>=340 and ball.distance(r_paddle)<50) or (ball.xcor()<=-340 and ball.distance(l_paddle)<50) :
        ball.colliwthpdl()
    #gone beyond paddle
    if ball.xcor()>=380 :
        ball.resetpos()
        scoreboard.lpoint()
    if ball.xcor()<=-380:
        ball.resetpos()
        scoreboard.rpoint()
screen.exitonclick()   