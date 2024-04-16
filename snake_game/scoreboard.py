from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle()
        self.pencolor("white")
        self.score = 0
        self.highscore = self.read_highscore()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.score = 0
        self.update_scoreboard()

    def save_highscore(self):
        with open("highscore.txt", mode="w") as file:
            file.write(str(self.highscore))

    def read_highscore(self):
        with open("highscore.txt", mode="r") as file:
            highscore = int(file.read())
            return highscore
