import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


def create_writing(x_coord, y_coord, state):
    writing = turtle.Turtle()
    writing.hideturtle()
    writing.penup()
    writing.goto(x=x_coord, y=y_coord)
    writing.write(arg=state, align="center", font=("Courier", 10, "normal"))


data = pandas.read_csv("50_states.csv")

# loop
guessed_states = []

while len(guessed_states) < 50:

    # Get user input
    correct_states = len(guessed_states)
    answer_state = screen.textinput(title=f"{correct_states}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # Check if it is correct
    all_states = data.state.to_list()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        data_row = data[data.state == answer_state]
        x_cor = int(data_row.x)
        y_cor = int(data_row.y)
        state = str(data_row.state)
        create_writing(x_coord=x_cor, y_coord=y_cor, state=data_row.state.item())
        guessed_states.append(answer_state)
