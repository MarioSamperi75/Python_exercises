from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('black')
        self.setheading(90)
        self.restart()


    def move(self):
        self.forward(MOVE_DISTANCE)

    def restart(self):
        self.goto(0, -280)

    def is_winner(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False




