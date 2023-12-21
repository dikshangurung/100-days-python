from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard
scoreboard = Scoreboard()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)
screen.title("Pong")
screen.listen()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
game_on = True
while game_on:
    time.sleep(ball.move_speed )
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(l_paddle) < 50 and ball.xcor()<-320 or ball.distance(r_paddle) < 50 and ball.xcor() >320:
        ball.bounce_x()
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()
    screen.update()


screen.exitonclick()