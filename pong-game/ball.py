from turtle import Turtle

class Ball(Turtle):
    def __init__(self, shape: str = "classic") -> None:
        super().__init__(shape)
        self.penup()
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.velocity = 0.1
        
    def move(self):
        self.goto(self.xcor()+self.x_move , self.ycor()+self.y_move)
       
    def bounce(self):
        self.y_move *= -1

    def bounce_back(self):
        self.x_move *= -1
        self.velocity * 0.9
        
    def reset(self):
        self.goto(0, 0)
        self.bounce_back()
        self.velocity = 0.1