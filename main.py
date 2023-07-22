import time
from file_update import Fileupdate
from snake import *
from turtle import Turtle, Screen
from food import Food
from scoreboard import Score

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")

screen.tracer(0)
food = Food()
update_file = Fileupdate()
snake = Snake()
score = Score()

screen.listen()
screen.onkey(fun=snake.up1, key="Up")
screen.onkey(fun=snake.down1, key="Down")
screen.onkey(fun=snake.left1, key="Left")
screen.onkey(fun=snake.right1, key="Right")

score.print_score(update_file.score)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with Food
    if snake.new_turtles[0].distance(food) < 15:
        food.refresh()
        score.increase_score()
        score.print_score(update_file.score)
        snake.extend()

    # Detect Collision with Wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() < -290 or snake.head.ycor() > 300:
        game_on = False
        score.game_over()

    for segment in snake.new_turtles[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
