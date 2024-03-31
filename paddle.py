from turtle import Turtle

WIDTH = 5
HEIGHT = 1


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.y = 0
        self.color('white')
        self.shape('square')
        self.penup()
        self.speed('fastest')
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)

    def move_up(self):
        if 280 > round(self.ycor()):
            y = 20 + self.ycor()
            x = self.xcor()
            self.goto(x, y)

    def move_down(self):
        if round(self.ycor()) > -280:
            y = self.ycor() - 20
            x = self.xcor()
            self.goto(x, y)
