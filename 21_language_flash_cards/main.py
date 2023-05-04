import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

words_to_learn = data.to_dict(orient="records")


def on_right_btn_click():
    words_to_learn.remove(current_card)
    new_dataframe = pandas.DataFrame.from_dict(words_to_learn)
    new_dataframe.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global timer
    global current_card
    windows.after_cancel(timer)

    current_card = random.choice(words_to_learn)
    french_word = current_card['French']

    canvas.itemconfig(image, image=cart_front_img)
    canvas.itemconfig(language, text='French', fill="black")
    canvas.itemconfig(word, text=french_word, fill="black")
    timer = windows.after(3000, show_back)


def show_back():
    canvas.itemconfig(image, image=cart_back_img)
    english_word = current_card['English']
    canvas.itemconfig(language, text='English', fill="white")
    canvas.itemconfig(word, text=english_word, fill="white")



windows = Tk()
windows.title("Flashy")
windows.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
cart_front_img = PhotoImage(file="images/card_front.png")
cart_back_img = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 263, image=cart_front_img)
language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=on_right_btn_click)
right_btn.grid(row=1, column=0)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=1)
timer = windows.after(3000, show_back)
next_card()
windows.mainloop()
