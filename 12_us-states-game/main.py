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

states = data.state.to_list()
right_answers = []
score = 0
states_nr = len(states)

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

    if guess == "Exit":
        break
    if guess in states and guess not in right_answers:
        # get coordinates
        row = data[data.state == guess]
        # iloc[0] instead of get[0] to not have deprecation warning
        x = int(row.x.iloc[0])
        y = int(row.y.iloc[0])

        # updating list right answers
        right_answers.append(guess)

        # updating score
        score = len(right_answers)

        # write text in the map
        USState(guess, x, y)


missing_states = states
for item in right_answers:
    missing_states.remove(item)


# alternative
# missing_states = []
# for state in states:
#     if state not in right_answers:
#         missing_states.append(state)

df = pandas.DataFrame(missing_states)
df.to_csv("missing.csv")
