from turtle import Turtle

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

    
    
    
    
