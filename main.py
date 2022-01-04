from turtle import Turtle, Screen
from scoreboard import Scoreboard
import time
from paddle import Paddle
from ball import Ball

scoreboard = Scoreboard()
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.update()

tim = Turtle()
tim.color('white')
tim.hideturtle()
tim.penup()
screen.tracer(0)
tim.goto(0, 300)
tim.setheading(270)
tim.speed('fastest')
ball = Ball()

for _ in range(30):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)

l_paddle = Paddle((-370, 0))
r_paddle = Paddle((360, 0))

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

while scoreboard.score_user1 < 5 and scoreboard.score_user2 < 5:
    ball.start_ball()
    while True:
        time.sleep(0.01)
        ball.move()
        if ball.ycor() >= 280 or ball.ycor() <= -280:
            ball.wall_bounce()
        if ball.xcor() >= 340 and ball.ycor() + 50 > r_paddle.ycor() > ball.ycor() - 50:
            ball.paddle_bounce()
        if ball.xcor() <= -350 and ball.ycor() + 50 > l_paddle.ycor() > ball.ycor() - 50:
            ball.paddle_bounce()
        elif ball.xcor() >= 360:
            scoreboard.increase_score_user1()
            break
        elif ball.xcor() <= -380:
            scoreboard.increase_score_user2()
            break
        screen.update()


screen.exitonclick()