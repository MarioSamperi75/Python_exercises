from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.read_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def read_high_score(self):
        # "C:/Users/mario/OneDrive/Desktop/data.txt" - absolute path
        with open("../../../../OneDrive/Desktop/data.txt") as file:
            self.high_score = int(file.read())

    def write_high_score(self, score):
        # "C:/Users/mario/OneDrive/Desktop/data.txt" -absolute path
        with open("../../../../OneDrive/Desktop/data.txt", mode="w") as file:
            file.write(str(score))
