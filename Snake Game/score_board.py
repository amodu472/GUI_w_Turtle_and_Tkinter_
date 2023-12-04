from turtle import Turtle


class ScoreBoard(Turtle):
    """This class inherits from the Turtle class to display the player's current in-game score and overall high score"""
    def __init__(self):
        super().__init__()
        self._score = 0
        with open("data.txt") as score:
            self._high_score = int(score.read())
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self._score}  High Score: {self._high_score}", move=False, align='center',
                   font=('Arial', 12, 'bold'))

    def update(self):
        self._score += 1

    def set_scores(self):
        if self._score > self._high_score:
            self._high_score = self._score
            with open("data.txt", "w") as high_score:
                high_score.write(str(self._high_score))
        self._score = 0
        self.write_score()
