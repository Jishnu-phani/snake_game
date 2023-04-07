from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('/Users/jishn/OneDrive/Desktop/data.txt') as data:
            self.high_score = int(data.read())
        self.temporary_high_score = self.high_score
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.temporary_high_score}", align="center", font=("Arial", 15, "normal"))
        self.hideturtle()

    def update_score(self):
        self.clear()
        # self.score += 1
        self.write(f"Score: {self.score} High Score: {self.temporary_high_score}", align="center", font=("Arial", 15, "normal"))

    def reset(self):
        if self.score > self.temporary_high_score:
            self.temporary_high_score = self.score
            with open('/Users/jishn/OneDrive/Desktop/data.txt', mode='w') as data:
                data.write(f'{self.score}')
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game over.", align="center", font=("Arial", 15, "normal"))
