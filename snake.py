from turtle import Turtle


class Snake:

    def __init__(self):
        self.turtles = []
        self.snake()

    def snake(self):

        for i in range(3):
            turtle = Turtle()
            turtle.penup()
            turtle.shape("square")
            turtle.color("white")
            turtle.goto(-20*i, 0)
            self.turtles.append(turtle)
        return self.turtles

    def add_segment(self, position):
        turtle = Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.color("white")
        turtle.goto(position)
        self.turtles.append(turtle)

    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[i - 1].xcor()
            new_y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(new_x, new_y)
        self.turtles[0].forward(20)

    def up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)

    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)

    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)

    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)

    def reset(self):
        for seg in self.turtles:
            seg.hideturtle()
        self.turtles.clear()
        self.snake()
