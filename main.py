from turtle import Turtle,Screen
import pandas as pd


screen = Screen()
screen.title("Indian state Game")
image_path = "India_state.gif"
screen.addshape(image_path)
jkp = Turtle()
jkp.shape(image_path)

data = pd.read_csv("ind_state.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 29 :
    answer_state = screen.textinput(title=f"{len(guessed_states)}/29 State Correct", prompt="What's another state's name? ").title()
     
    if answer_state in all_states:
        guessed_states.append(answer_state)
        j = Turtle()
        j.hideturtle()
        j.penup()
        state_data = data[data.state == answer_state]
        j.goto(int(state_data.X), int(state_data.Y))
        j.write(answer_state)
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        df = pd.DataFrame(missing_states)
        df.to_csv("state to learn.csv")       
        break



