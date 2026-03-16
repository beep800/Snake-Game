from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.score=-1
        with open("high_score.txt") as file:
            self.highscore=int(file.read())
        self.update()

    def update(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score} High score: {self.highscore}", align="center", font=('Courier', 15,'normal'))

    def reset(self):
        if self.score>self.highscore:
            with open("high_score.txt", mode = "w") as file:
                file.write(str(self.score))
        self.score=-1
        self.update()

