from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, px, py) -> None:
        super().__init__()
        self.shape("square")
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(px, py)
        
    def go_up(self):
        new_y = self.ycor() + 20
        if new_y <= 240:
            self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = self.ycor() - 20
        if new_y >= -240:
            self.goto(self.xcor(), new_y)
    
    def reset(self):
        self.goto(self.xcor(), 0)      