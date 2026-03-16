from turtle import Turtle

UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create()
        self.head = self.snake_body[0]


    def create(self):
        x = 0
        for length in range(0, 3):
            new_part = Turtle(shape="square")
            new_part.color("white")
            new_part.penup()
            new_part.setx(x)
            x -= 20
            self.snake_body.append(new_part)


    def extend(self):
        new_part = Turtle(shape="square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(self.snake_body[-1].position())
        self.snake_body.append(new_part)

    def reset(self):
        for body_part in self.snake_body:
            body_part.hideturtle()
        self.snake_body.clear()
        self.create()
        self.head = self.snake_body[0]

    def move(self):
        for seg in range(len(self.snake_body) - 1, 0, -1):
            xcor = self.snake_body[seg - 1].xcor()
            ycor = self.snake_body[seg - 1].ycor()
            self.snake_body[seg].goto(xcor, ycor)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
