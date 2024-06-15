from turtle import Turtle
FONT = ('Courier', 32, 'normal')

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()
    
    def update_left(self):
        self.l_score += 1
        self.update()
        
    def update_right(self):
        self.r_score += 1
        self.update()
        
    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=FONT)