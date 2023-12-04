from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(position)
        self._score = 0
        self.write_score()

    def write_score(self):
        self.write(f"{self._score}", move=False, align='center', font=('Courier', 32, 'normal'))

    def update_score(self):
        self.clear()
        self._score += 1
        self.write_score()

