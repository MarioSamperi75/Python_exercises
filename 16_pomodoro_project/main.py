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

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Pomodoro")
windows.config(pady=50, padx=100, bg=YELLOW)

pom_img = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW)
canvas.create_image(102, 112, image=pom_img)
canvas.create_text(104, 132, text="00:00", fill="white", font=("Garamond", 30, "bold"))
canvas.pack()

windows.mainloop()
