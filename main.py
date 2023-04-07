import turtle
from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
turtle.delay(delay=None)

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)

    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        scoreboard.update_score()
        snake.extend()
        # snake.turtles.append()

    if snake.turtles[0].xcor() > 280 or snake.turtles[0].xcor() < -280 or snake.turtles[0].ycor() < -280 or \
            snake.turtles[0].ycor() > 280:
        # print("game over")
        scoreboard.reset()
        snake.reset()
        # scoreboard.game_over()
        # game_is_on = False

    for segment in snake.turtles[1:]:
        if snake.turtles[0].distance(segment) < 10:
            scoreboard.reset()
            # game_is_on = False
            # scoreboard.game_over()

screen.exitonclick()
