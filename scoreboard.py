from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_user1 = 0
        self.score_user2 = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(5, 260)
        self.update_scoreboard()

    def increase_score_user1(self):
        self.score_user1 += 1
        self.update_scoreboard()

    def increase_score_user2(self):
        self.score_user2 += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score_user1}          Score: {self.score_user2}', align='center', font=("Arial", 24, "normal"))








