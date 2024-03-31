from turtle import Turtle
from paddle import Paddle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('pink')
        self.penup()
        self.x_move = 1
        self.y_move = 1

    def move(self):
        new_x = self.x_move + self.xcor()
        new_y = self.y_move + self.ycor()
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1.4

    def paddle_bounce(self):
        self.x_move *= -1.4

    def out_of_bounds(self):
        if self.x_move < 0:
            self.x_move = 1
            self.y_move = 1
        else:
            self.x_move = -1
            self.y_move = -1

        self.goto(0,0)
        new_x = (self.x_move + self.xcor())
        new_y = (self.y_move + self.ycor())
        self.goto(new_x, new_y)
