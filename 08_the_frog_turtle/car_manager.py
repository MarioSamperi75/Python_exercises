import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []

    def create_a_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.car_speed = STARTING_MOVE_DISTANCE
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(1, 2)
        new_car.goto(260, random.randint(-250, 250))
        self.cars.append(new_car)

   # def move_car(self):
   #     self.setx(self.xcor() - self.car_speed)

   # def update_speed(self):
   #     self.car_speed += MOVE_INCREMENT
   #     print(self.car_speed)



