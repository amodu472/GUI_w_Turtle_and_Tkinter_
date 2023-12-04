from turtle import Turtle


class ScoreBoard(Turtle):
    """This class inherits from the turtle class and defines behaviour for a typical ScoreBoard system"""
    def __init__(self):
        super().__init__()
        self._level = 1
        self.hideturtle()
        self.penup()
        self.goto(-285, 265)
        self.write_level()

    def write_level(self):
        self.write(f"Level: {self._level}", move=False, align='left', font=('Courier', 12, 'bold'))

    def level_up(self):
        self.clear()
        self._level += 1
        self.write_level()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER!!!\nLEVEL: {self._level}", move=False, align='center', font=('Courier', 12, 'bold'))
