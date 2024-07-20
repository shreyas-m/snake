from turtle import Turtle


class Score(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=("Comic Sans MS", 24, "bold"))

    def refresh(self):
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=("Comic Sans MS", 24, "bold"))
