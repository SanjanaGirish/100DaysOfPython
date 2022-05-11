import turtle

FONT = ("Arial", 12, "normal")
screen = turtle.Screen()
tim = turtle.Turtle()
screen.title('US States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
tim.penup()
tim.hideturtle()

# How to get the coordinates of the states from image
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

import pandas
data = pandas.read_csv("50_states.csv")
states_lst = data["state"].to_list()
correct_guesses = []
answer_state = ''

while len(correct_guesses) <= 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                             prompt="What's another state name").title()
    if answer_state == 'Exit':
        break
    if answer_state in states_lst:
        correct_guesses.append(answer_state)
        row = data[data.state == answer_state]
        tim.goto(int(row.x), int(row.y))
        tim.write(arg=answer_state, font=FONT)

# Generate states to learn
missing_states = list(sorted(set(states_lst) - set(correct_guesses)))
missing_states_dict = {"States": missing_states}
dt = pandas.DataFrame(missing_states_dict)
dt.to_csv('states_to_learn.csv')
