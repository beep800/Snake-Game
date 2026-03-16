from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Sneeky boy")
screen.tracer(0)

snake = Snake()
food=Food()
scoreboard=Scoreboard()

def play_again():
    again = screen.textinput("Game Over", "Game over. Would you like to play again?")
    if again == "no":
        screen.bye()
    screen.listen()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_over=False
while not game_over:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update()

    if snake.head.xcor()>=300 or snake.head.xcor()<= -300 or snake.head.ycor()>=300 or snake.head.ycor()<= -300:
        scoreboard.reset()
        snake.reset()
        play_again()

    for part in snake.snake_body[1:]:
        if snake.head.distance(part)<10:
            scoreboard.reset()
            snake.reset()
            play_again()




screen.exitonclick()