import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

def on_press_right():
    pick_a_random_card()


def on_press_wrong():
    pick_a_random_card()


def pick_a_random_card():
    random_index = random.randrange(len(data.index))
    french_word = data.iloc[random_index, data.columns.get_loc('French')]
    english_word = data.iloc[random_index, data.columns.get_loc('French')]
    canvas.itemconfig(language, text='French')
    canvas.itemconfig(word, text=french_word)


data = pandas.read_csv("data/french_words.csv")
windows = Tk()
windows.title("Flashy")
windows.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
cart_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=cart_front_img)
language = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=on_press_right)
right_btn.grid(row=1, column=0)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=on_press_wrong)
wrong_btn.grid(row=1, column=1)


windows.mainloop()
