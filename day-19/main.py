from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

position = -40

all_turtle = []

for color in colors:
  tim = Turtle(shape="turtle")
  tim.color(color)
  tim.penup()
  tim.goto(x=-240, y=position)
  position+=30
  all_turtle.append(tim)
    

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() >= 220:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("Your guess is right you won")
                is_race_on = False
                break
            else:
                print(f"sorry you loose {turtle.pencolor()} won the race")
                is_race_on = False
                break
            
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




# def move_turtle_forward():
#     tim.forward(10)
    
# def move_turtle_backward():
#     tim.backward(10)
    
# def turn_left():
#     tim.left(10)
    
# def turn_right():
#     tim.right(10)
    
# def clear_every():
#     # tim.clear()
#     # tim.penup()
#     # tim.home()
#     # tim.pendown()
#     tim.reset()
    

# screen.listen()
# screen.onkey(key='w', fun=move_turtle_forward)
# screen.onkey(key='s', fun=move_turtle_backward)
# screen.onkey(key='a', fun=turn_left)
# screen.onkey(key='d', fun=turn_right)
# screen.onkey(key='c', fun=clear_every)
screen.exitonclick()