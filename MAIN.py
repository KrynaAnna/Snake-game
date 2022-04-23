from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
from sounds import *


def update_screen():
    screen = Screen()
    screen.colormode(255)
    screen.bgcolor('pale turquoise')
    screen.setup(width=600, height=600)
    screen.title('My snake game')
    screen.tracer(0)


def game():
    screen = Screen()
    screen.clear()
    update_screen()
    food = Food()
    snake = Snake()
    scoreboard = Scoreboard()

    # Keyboard
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(game, "space")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food.
        if snake.head.distance(food) < 20:
            eating_sound()
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall.
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            over_sound()
            game_is_on = False
            scoreboard.game_over()
            scoreboard.maximum()

        # Detect collision with tail.
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
                scoreboard.maximum()

    screen.exitonclick()


game()
