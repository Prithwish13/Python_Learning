from turtle import Turtle
import random

def makeSquare(selected_turtle: Turtle) -> None:
    for _ in range(4):
       selected_turtle.forward(100)
       selected_turtle.right(90)
       
def drawDashedLine(selected_turtle: Turtle) -> None:
    for _ in range(10):
        selected_turtle.pendown()
        selected_turtle.forward(10)
        selected_turtle.penup()
        selected_turtle.forward(10)
        
def drawShape(selected_turtle: Turtle, arms: int, color: str) -> None:
    selected_turtle.color(color)
    for _ in range(arms):
        selected_turtle.forward(100)
        selected_turtle.right(float(360/arms))
        
def random_turtle_color() -> str:
    # Generate random RGB values
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    # Convert RGB values to hexadecimal color code
    color_code = "#{:02x}{:02x}{:02x}".format(red, green, blue)
    return color_code
    

def randomWalk(selected_turtle: Turtle, input_steps: int) -> None:
    selected_turtle.pensize(10)
    for _ in range(input_steps):
        selected_turtle.color(random_turtle_color())
        step = int(random.random() * input_steps)
        angle = int(random.random() * 360)
        selected_turtle.forward(step)
        selected_turtle.right(angle)
        selected_turtle.forward(step)
        selected_turtle.left(angle)
        
def make_spiral(selected_turtle: Turtle, input_steps: int) -> None:
    for _ in range(45):
        selected_turtle.color(random_turtle_color())
        selected_turtle.circle(100)
        # selected_turtle.left(8)
        selected_turtle.setheading(selected_turtle.heading() + 8)

    
    
