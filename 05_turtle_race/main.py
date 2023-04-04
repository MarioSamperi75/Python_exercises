from turtle import Turtle, Screen

tim = Turtle()
tim.speed(0)

def move_forward():
    tim.forward(10)


def move_backward():
    tim.forward(-10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def reset_position():
    tim.reset()
    tim.clear()


screen = Screen()
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset_position)
screen.exitonclick()
