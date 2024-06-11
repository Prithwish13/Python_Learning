from turtle import Screen, Turtle
import time

# constants
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = "stop"
        
    def create_snake(self) -> None:
         for position in STARTING_POSITION:
            self.add_segment(position=position)
       
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
        
    def up(self):
        if self.direction != "down":
            self.head.setheading(UP)
            self.direction = "up"

    def down(self):
        if self.direction != "up":
            self.head.setheading(DOWN)
            self.direction = "down"

    def left(self):
        if self.direction != "right":
             self.head.setheading(LEFT)
             self.direction = "left"

    def right(self):
        if self.direction != "left":
             self.head.setheading(RIGHT)
             self.direction = "right"
    
    def add_segment(self, position):
        snake_body = Turtle(shape="square")
        snake_body.penup()
        snake_body.color('white')
        snake_body.goto(position)
        self.segments.append(snake_body)
             
    def extend(self):
        self.add_segment(self.segments[-1].position())