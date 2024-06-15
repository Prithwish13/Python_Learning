from turtle import Screen, Turtle;
from paddle import Paddle;
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


paddle_right = Paddle(px=350, py=0)
paddle_left = Paddle(px=-350, py=0)
ball = Ball(shape="circle")
score_board = Scoreboard()

screen.listen()
screen.onkey(paddle_right.go_up, 'Up')
screen.onkey(paddle_right.go_down, 'Down')

screen.onkey(paddle_left.go_up, 'w')
screen.onkey(paddle_left.go_down, 's')



game_is_on = True

while game_is_on:
    time.sleep(ball.velocity)
    ball.move()
    if ball.xcor() > 320 and  paddle_right.distance(ball) <= 50:
       ball.bounce_back()
       
    if ball.xcor() < -320 and paddle_left.distance(ball) <= 50:
       ball.bounce_back()
    
    if ball.xcor() > 360:
        ball.reset()
        paddle_left.reset()
        paddle_right.reset()
        score_board.update_left()
        
    if ball.xcor() < -360:
        ball.reset()
        paddle_left.reset()
        paddle_right.reset()
        score_board.update_right()
        
       
    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
       ball.bounce()
        
    screen.update()



screen.exitonclick()