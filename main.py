from turtle import Screen, Turtle
import pandas

screen = Screen()

turtle = Turtle()

screen.title("U.S States Game")
screen.setup(width=740, height=500)
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

csv_data_states = pandas.read_csv("50_states.csv")
states = csv_data_states["state"]
input_list = []
s_list = states.to_list()
num = 0
game_on = True
while game_on:

    input_state = screen.textinput(title=f"{num}/50 states correct", prompt="Type a state's name").title()
    if input_state in s_list:
        input_list.append(input_state)

        csv_state = csv_data_states[states == input_state]

        csv_state_xcor = int(csv_state["x"])
        csv_state_ycor = int(csv_state["y"])

        letter_turtle = Turtle()

        letter_turtle.hideturtle()

        letter_turtle.penup()
        letter_turtle.goto(x=csv_state_xcor, y=csv_state_ycor)
        letter_turtle.write(input_state)
        num += 1
        if num == 50:
            break
    elif input_state == "End Game":
        missed_names = [name for name in s_list if name not in input_list]
        missed_names_data = pandas.DataFrame(missed_names, columns=["missed_states"])
        csv_missed_states = missed_names_data.to_csv("missed_names.csv")

        break
