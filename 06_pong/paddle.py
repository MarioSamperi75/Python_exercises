from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        self.paddle = Turtle('square')
        self.paddle.penup()
        self.paddle.color('white')
        self.paddle.turtlesize(5, 1)
        self.paddle.goto(350, 0)

    def move_up(self):
        self.paddle.sety(self.paddle.ycor() + 20)

    def move_down(self):
        self.paddle.sety(self.paddle.ycor() - 20)
