from turtle import Turtle, Screen

screen = Screen()
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    new_turtles = []

    def __init__(self):
        super().__init__()
        x_co = 0
        self.game_on = True
        self.extra_count = 0
        for i in range(3):
            tim = Turtle(shape="square")
            tim.color("white")
            tim.penup()
            tim.goto(x_co, 0)
            x_co += -20
            Snake.new_turtles.append(tim)

        self.head = Snake.new_turtles[0]

    def extend(self):
        tim = Turtle()
        tim.shape("square")
        tim.color("white")
        tim.penup()
        x = self.new_turtles[2 + self.extra_count].xcor()
        y = self.new_turtles[2 + self.extra_count].ycor()
        tim.goto(x, y)
        self.extra_count += 1
        Snake.new_turtles.append(tim)

    def up1(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down1(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left1(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right1(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def move(self):
        """
This function Continuously moves the snake forward
        """
        for i in range(len(Snake.new_turtles) - 1, 0, -1):
            new_xcor = Snake.new_turtles[i - 1].xcor()
            new_ycor = Snake.new_turtles[i - 1].ycor()
            Snake.new_turtles[i].goto(x=new_xcor, y=new_ycor)
        self.head.forward(20)
