# import colorgram
# rgb_colors = []
# colors = colorgram.extract("hirst_img.jpeg", 30)

# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

import turtle as turtle_module
import random

turtle_module.colormode(255)
timmy = turtle_module.Turtle()
timmy.hideturtle()
    
color_list = [(244, 235, 48), (196, 12, 35), (218, 160, 70), (43, 80, 177), (237, 40, 140), (38, 215, 76),
              (237, 228, 5), (31, 40, 154), (206, 72, 22), (21, 149, 23), (201, 34, 98), (70, 11, 27), (182, 16, 11),
              (213, 164, 10), (218, 140, 195), (56, 15, 10), (17, 20, 48), (13, 95, 62), (79, 210, 159), (73, 73, 221), (83, 191, 220),
              (237, 158, 216), (94, 232, 200), (217, 82, 51), (5, 230, 239), (14, 64, 44)]
def move_and_draw ():
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)

def go_back ():
   timmy.setheading(90)
   timmy.forward(50)
   timmy.setheading(180)
   timmy.forward(500)
   timmy.setheading(0)


# first set the positions
timmy.penup()

timmy.setheading(220)
timmy.forward(300)
timmy.setheading(0)

for _ in range(10):
    move_and_draw()
    go_back()







screen = turtle_module.Screen()
screen.exitonclick()