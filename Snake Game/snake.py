from turtle import Turtle


class Snake:
    STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20
    """This class models the snake appearance and its behaviours during gameplay"""

    def __init__(self):
        # List of starting positions stored as tuples
        self._segments = []
        self.initialize()
        self._head = self._segments[0]

    @property
    def head(self):
        return self._head

    def initialize(self):
        # Loop through the starting positions, creating one segment for each position
        for position in Snake.STARTING_POSITION:
            self.create_segment(position)

    def create_segment(self, position):
        # Creates a snake segment
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self._segments.append(segment)

    def extend(self):
        self.create_segment(self._segments[-1].position())

    def move(self):
        # The movement simulation for the different segments. NOTE: It's important that the fd distance is 20px!
        for seg in range(len(self._segments) - 1, 0, -1):
            x_cor = self._segments[seg - 1].xcor()
            y_cor = self._segments[seg - 1].ycor()
            self._segments[seg].goto(x_cor, y_cor)
        self._head.fd(self.MOVE_DISTANCE)

    def tail_collision(self):
        # Detect head - tail/mid-section collision
        for seg in self._segments[1:]:
            if self._head.distance(seg) < 10:
                return True
            else:
                continue

    def reset_(self):
        for seg in self._segments:
            seg.goto(1000, 1000)
        self._segments.clear()
        self.initialize()
        self._head = self._segments[0]

    def left(self):
        if self._head.heading() != 0:
            self._head.seth(180)

    def right(self):
        if self._head.heading() != 180:
            self._head.seth(360)

    def down(self):
        if self._head.heading() != 90:
            self._head.seth(270)

    def up(self):
        if self._head.heading() != 270:
            self._head.seth(90)
