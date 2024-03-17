from turtle import Turtle, Screen
import heroes
from movements import makeSquare,drawDashedLine, drawShape

the_turtle = Turtle()
the_turtle.shape("turtle")
# the_turtle.color("light salmon")

# makeSquare(the_turtle)
# drawDashedLine(the_turtle)

# print(heroes.gen())
drawShape(the_turtle, 3, "thistle")
drawShape(the_turtle, 4, "orange red")
drawShape(the_turtle, 5, "medium violet red")
drawShape(the_turtle, 6, "gold")
drawShape(the_turtle, 7, "lime")
drawShape(the_turtle, 8, "red")
drawShape(the_turtle, 9, "blue")
drawShape(the_turtle, 10, "pink")



screen = Screen()
screen.exitonclick()