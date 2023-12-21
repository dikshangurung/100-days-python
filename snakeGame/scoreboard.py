from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.penup()
        with open("data.txt", mode="r") as file:
            self.highScore = int(file.read())
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} High Score: {self.highScore}", False, align="center", font=('Arial', 20, 'normal'))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", False, align="center", font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("data.txt",mode="w") as file:
                file.write(f"{self.highScore}")
        self.score = -1