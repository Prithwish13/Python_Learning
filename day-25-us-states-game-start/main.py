import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
guess_states = []

# this could be a way
# data['state'] = data["state"].str.lower()
all_states = data.state.to_list()
# all_state_lower = [state.lower() for state in all_states]


while len(guess_states) < 50:
 answer_state =  screen.textinput(title=f"{len(guess_states)}/50 States Correct", prompt="what is another state name").title()
 if answer_state == "Exit":
     missing_stats = [state for state in all_states if state not in guess_states]
     new_data = pandas.DataFrame(missing_stats)
     new_data.to_csv("states_to_learn.csv")
     break
 if answer_state in all_states: 
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(state_data.x.item(), state_data.y.item())
    t.write(state_data.state.item())
    guess_states.append(answer_state)





# turtle.mainloop()

# screen.exitonclick()