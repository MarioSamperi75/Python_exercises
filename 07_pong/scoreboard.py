from turtle import Turtle

FONT = ('Courier', 80, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 180)
        self.refresh_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.refresh_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score}  -  {self.r_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)