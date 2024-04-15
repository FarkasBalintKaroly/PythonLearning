from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Creating the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong game")

screen.listen()
screen.tracer(0)

# creating the objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# listening to user inputs
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True
r_score = 0
l_score = 0

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # detect collision to top and bottom wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 \
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320:

        ball.bounce_x()

    # detect when paddle misses the ball
    # if R paddle misses the ball
    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.reset_position()
        ball.bounce_x()

    # if L paddle misses the ball
    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.reset_position()
        ball.bounce_x()

screen.exitonclick()
