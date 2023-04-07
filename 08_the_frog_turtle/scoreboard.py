from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-270, 250)
        self.refresh_scoreboard()

    def level_up(self):
        self.level += 1
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(f"Level {self.level}", font=FONT)

    def show_game_over(self):
        game_over = Turtle()
        game_over.hideturtle()
        game_over.clear()
        game_over.color("black")
        game_over.write("GAME OVER", font=FONT, align="center")
        game_over.penup()
        game_over.goto(0, 0)




