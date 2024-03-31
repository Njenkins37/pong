from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

LX = -180
Y = 250
RX = 180


def create_midline():
    t = Turtle()
    t.color('white')
    t.pencolor('white')
    t.penup()
    t.setx(0)
    t.sety(360)
    t.seth(270)
    for i in range(17):
        t.pendown()
        t.fd(20)
        t.penup()
        t.fd(20)


if __name__ == '__main__':
    screen = Screen()
    screen.bgcolor('black')
    screen.setup(width=800, height=620)
    screen.title('Pong')
    screen.listen()
    screen.tracer(0)

    create_midline()

    r_paddle = Paddle()
    r_paddle.goto(350, r_paddle.y)

    screen.onkey(r_paddle.move_up, "Up")
    screen.onkey(r_paddle.move_down, 'Down')

    l_paddle = Paddle()
    l_paddle.goto(-350, l_paddle.y)
    screen.onkey(l_paddle.move_up, 'w')
    screen.onkey(l_paddle.move_down, 's')
    ball = Ball()

    game_is_on = True
    l_score = Scoreboard()
    r_score = Scoreboard()

    l_score.goto(LX, Y)
    r_score.goto(RX, Y)

    while game_is_on:

        l_score.write(arg=f'Score: {l_score.score}', font=('courier', 24, 'normal'), move=False, align='center')
        r_score.write(arg=f'Score: {r_score.score}', font=('courier', 24, 'normal'), move=False, align='center')

        if ball.ycor() > 300 or ball.ycor() < -300:
            ball.bounce()

        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320
                or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.paddle_bounce()

        if ball.xcor() > 380:
            ball.out_of_bounds()
            l_score.add_score()
            l_score.clear()

        if ball.xcor() < -380:
            ball.out_of_bounds()
            r_score.add_score()
            r_score.clear()

        ball.move()

        screen.update()

    screen.exitonclick()
