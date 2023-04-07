# create the turtle and the turtle movement
import random
# create the car and the car movement

# Scoreboard level 1: methode to update

# Turtle at the end: restart position,  update level, speed car

# Crossing the car: game over

# instanciate new car: random time, position, color


import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
car_manager = CarManager()
player = Player()
screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    car_manager.move_cars()

    if player.is_winner():
        scoreboard.level_up()
        player.restart()
        car_manager.update_speed()

    if random.randint(1, 10) > 8:
        car_manager.create_a_car()

    time.sleep(0.1)
    screen.update()
