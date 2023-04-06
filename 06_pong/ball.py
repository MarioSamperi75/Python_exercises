from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('darkred')
        self.penup()

    def move(self):
        new_x = self.xcor() + 0.4
        new_y = self.ycor() + 0.3
        self.goto((new_x, new_y))


