from turtle import Turtle
from time import sleep

RIGHT = 0

LEFT = 180

UP = 90
DOWN = 270


class Snake:
    snake_parts = []
    head = Turtle()

    def __init__(self):
        for i in range(0, 3):
            self.add_segment((-20 * i, 0))
            self.head = self.snake_parts[0]

    def move(self):
        sleep(0.1)
        for position in range(len(self.snake_parts) - 1, 0, -1):
            self.snake_parts[position].goto(self.snake_parts[position - 1].xcor(), self.snake_parts[position - 1].ycor())
        self.head.forward(10)

    def add_segment(self, position):
        snake_part = Turtle("square")
        snake_part.color('white')
        snake_part.penup()
        snake_part.goto(position)
        self.snake_parts.append(snake_part)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segment(self.snake_parts[-1].position())
