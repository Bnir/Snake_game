from turtle import Turtle
from file_update import Fileupdate
FONT = ("Arial", 16, "normal")
ALIGNMENT = "center"
CUURENT_SCORE_LOC = (-60, 260)
HIGH_SCORE_LOC = (60, 260)
file_update = Fileupdate()
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("grey")
        self.hideturtle()
        self.count = 0
        self.penup()

    def increase_score(self):
        self.count += 1
        self.clear()

    def print_score(self, high_score):
        self.penup()
        self.goto(CUURENT_SCORE_LOC)
        self.write(arg=f"Score: {self.count}", align= ALIGNMENT, move=False, font= FONT)
        self.goto(HIGH_SCORE_LOC)
        self.write(arg =f"High Score: {high_score}", align= ALIGNMENT, move=False, font= FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over", align= ALIGNMENT, move=False, font= FONT)
        file_update.check_high(self.count)



