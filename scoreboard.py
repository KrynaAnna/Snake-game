from turtle import Turtle
max_score = 0


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update()

    def update(self):
        self.goto(0, 260)
        self.write(arg=f'Score:{self.score}', align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.color('black')
        self.goto(0, 0)
        self.write(arg='GAME OVER', align="center", font=("Arial", 30, 'bold'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score:{self.score}', align="center", font=("Arial", 20, "normal"))

    def maximum(self):
        global max_score
        if self.score > max_score:
            max_score = self.score
        self.goto(220, 260)
        self.color('green')
        self.write(arg=f'Best score:{max_score}', align="center", font=("Arial", 15, "normal"))
