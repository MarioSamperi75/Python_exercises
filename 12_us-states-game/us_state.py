from turtle import Turtle


class USState(Turtle):

    def __init__(self, name, x_coor, y_coor):
        super().__init__()
        self.name = name
        self.color("black")
        self.penup()
        self.goto(x_coor, y_coor)
        self.write(name, align="center", font=("Courier", 10, "normal"))
        self.hideturtle()