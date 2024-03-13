import second_module
from turtle import Turtle, Screen
from random import random
from prettytable import PrettyTable

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     timmy.right(angle)
#     timmy.fd(steps)

# my_screen =  Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# print(second_module.variable)

# pretty table example

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmender"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align="l"
# table.align["Pokemon Name"] = "l"
# table.align["Type"] = "l"
print(table)