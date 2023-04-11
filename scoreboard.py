from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 40, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 240)
        self.l_score = 0
        self.r_score = 0
        self.refresh()

    def update_score_l(self):
        self.l_score += 1
        self.refresh()

    def update_score_r(self):
        self.r_score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"{self.l_score}\t{self.r_score}", align=ALIGNMENT, font=FONT)
