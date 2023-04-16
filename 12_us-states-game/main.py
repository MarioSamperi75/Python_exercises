import string
import turtle
from turtle import textinput
import pandas as pandas

from us_state import USState

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

state_series = data.state
right_answers = []
score = len(right_answers)
states_nr = len(state_series)

screen.title("U.S. States Game")


# do en input loop
# get the csv
# check the name
# if it exists get the rows, and the coordinates
# create the score
# update the score
# write the text in the map using the coordinates


while True:
    guess = textinput(title=f"{score}/{states_nr} Guess the State", prompt="What's another state's name?").title()
    # answer_state = string.capwords(turtle.textinput(title="Guess the State", prompt="What's another state's name?"))

    if guess in state_series.unique() and guess not in right_answers:
        # get coordinates
        row = data[state_series == guess]
        x = int(row.x)
        y = int(row.y)

        # updating list right answers
        right_answers.append(guess)

        # write text in the map
        USState(guess, x, y)


turtle.mainloop()
