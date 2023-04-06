from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('darkred')
        self.penup()
        self.x_mov = 0.6
        self.y_mov = 0.6

    def move(self):
        new_x = self.xcor() + self.x_mov
        new_y = self.ycor() + self.y_mov
        self.goto((new_x, new_y))

    def bounce(self):
        self.y_mov *= -1



