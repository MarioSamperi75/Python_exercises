from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):

        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_block = Turtle('square')
            new_block.color("white", "white")
            new_block.penup()
            new_block.goto(position)
            self.segments.append(new_block)

    def move(self):
        # all the segments go on 1 position in the list
        # starting with the last one
        # just the first one change direction
        for i in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
