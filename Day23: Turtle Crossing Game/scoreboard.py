from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.penup()
        self.goto(x=0, y=260)
        self.write(f"Level: {self.level}", align='center',
                   font=FONT)
        self.hideturtle()

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align='center',
                   font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER.", align='center', font=FONT)
