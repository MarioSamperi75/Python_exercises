from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_a_car()



    def create_a_car(self):
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.goto(260, 0)


    def move_car(self):
        self.setx(self.xcor() - STARTING_MOVE_DISTANCE)


