from turtle import Turtle

FONT = ('Courier', 24, 'normal')
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.refresh_scoreboard()


    def update_score(self):
        self.score += 1
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
