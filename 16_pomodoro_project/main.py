import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 


# ---------------------------- TIMER MECHANISM --------------------------- #
def start():
    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------ #
def count_down(count):
    minutes = math.floor(count/60)
    seconds = count % 60

    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    if count > 0:
        windows.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Pomodoro")
windows.config(pady=50, padx=100, bg=YELLOW)

pom_img = PhotoImage(file="tomato.png")

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, 'bold'))
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=pom_img)
timer = canvas.create_text(103, 132, text="00:00", fill="white", font=("Garamond", 30, "bold"))
canvas.grid(row=1, column=1)


start_btn = Button(text="Start", command=start)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset")
reset_btn.grid(row=2, column=2)

check_label = Label(text="✔", bg=YELLOW, fg=GREEN)
check_label.grid(row=3, column=1)

windows.mainloop()
