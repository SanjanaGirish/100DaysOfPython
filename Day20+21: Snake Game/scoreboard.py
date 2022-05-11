from turtle import Turtle
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('highscore_data.txt', mode='r') as f:
            self.high_score = int(f.read())
        self.color('white')
        self.penup()
        self.goto(x=0, y=280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('highscore_data.txt', mode='w') as f:
                f.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()



    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("GAME OVER.", align='center', font=FONT)
