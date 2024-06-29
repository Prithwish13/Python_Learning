from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)
starting_position = [(0, 0), (-20, 0), (-40, 0)]

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

    
game_is_on = True

while game_is_on:   
    screen.update()
    time.sleep(0.2)
    snake.move()
    
    # Detect collision with food
    
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    
    # Detect collision with the wall
    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()

    if x_cor > 280 or x_cor < -280 or y_cor > 280 or y_cor < -280:
    #    game_is_on = False
       score.reset()
       snake.reset()
       
    # Detect tail collision
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            score.reset()
            snake.reset()

screen.exitonclick()
        
        



