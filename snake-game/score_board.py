from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 18, 'normal')

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            content = file.read()
            self.high_score = int(content) if content else 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 280)
        self.score_update()
        
        
    
    def score_update(self):
        self.clear()
        self.write(f'Score:  {self.score} High score {self.high_score}', 
                   move=False, 
                   align=ALIGNMENT, 
                   font=FONT
                  )
        
    def increase_score(self):
        self.score += 10
        self.score_update()
        
    def reset(self): 
         if self.score > self.high_score:
             self.high_score = self.score
             with open("data.txt", mode="w") as file:
                file.write(str(self.score))
         self.score = 0
         self.score_update()
        
        
    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("Game Over", 
    #                move=False, 
    #                align=ALIGNMENT, 
    #                font=FONT
    #             )
    
        