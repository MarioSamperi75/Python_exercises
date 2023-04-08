import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.freq_car = 10

    def create_a_car(self):
        if random.randint(1, self.freq_car) > 8:
            new_car = Turtle("turtle")
            new_car.penup()
            new_car.car_speed = STARTING_MOVE_DISTANCE
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2)
            new_car.goto(260, random.randint(-250, 250))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            #car.setx(car.xcor() - self.car_speed)
            car.forward(self.car_speed)

    def is_crashed(self, player):
        for car in self.cars:
            if player.distance(car) < 20:
                return True
        return False

    def destroy_cars(self):
        for car in self.cars:
            if car.xcor() < -350:
                self.cars.remove(car)

    def update_speed(self):
        self.car_speed += MOVE_INCREMENT
        self.freq_car += 1




