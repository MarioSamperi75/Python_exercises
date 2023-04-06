from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('darkred')
        self.penup()
        self.x_mov = 2
        self.y_mov = 2
        self.speed = 0.01


    def restart(self):
        self.goto(0, 0)
        self.bounce_paddle()
        self.speed = 0.01


    def move(self):
        new_x = self.xcor() + self.x_mov
        new_y = self.ycor() + self.y_mov
        self.goto((new_x, new_y))

    def bounce_wall(self):
        self.y_mov *= -1

    def bounce_paddle(self):
        self.x_mov *= -1
        if self.speed > 0.001:
            self.speed -= 0.0003



