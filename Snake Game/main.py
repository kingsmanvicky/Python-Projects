from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Nokia's- THE SNAKE")
screen.tracer(0)


snake = Snake()
food = Food()
score = ScoreBoard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Collision with food:
    if snake.head.distance(food) < 15:
        food.refresh() 
        score.increase_score()
        snake.extend()
    
    #Detect collision with wall:
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        score.game_over()

    
    #Detect head and tail collision:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()