import turtle
import pandas
import pandas as pd

screen= turtle.Screen()
screen.title("U.S. States Guesser")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_is_on = True
ans_count = 0
TOTAL_STATES = 50
answered_states = []


#create dataframe
df = pandas.read_csv("50_states.csv")
states = df.state
states_list = states.to_list()
#create function for state assignment
def assign(guessed_state):
    i = turtle.Turtle()
    i.hideturtle()
    i.penup()
    x_coor = df[states == guessed_state].x.iloc[0]
    y_coor = df[states == guessed_state].y.iloc[0]
    i.goto(x_coor, y_coor)
    i.color("black")
    i.write(arg= f"{df[states == guessed_state].state.item()}", align="center", font=("Arial", 8, "normal"))

#main loop
while game_is_on:
    if ans_count ==0:
        answer_state = screen.textinput("Guess the state", "What's another state's name?").title()
    else:
        answer_state = screen.textinput(f"{ans_count}/{TOTAL_STATES} States Correct", "What's another state's name?").title()
    if answer_state in states_list:
        ans_count+= 1
        answered_states.append(answer_state)
        assign(answer_state)
    elif answer_state == "Exit":
        game_is_on = False
        #save missing states to csv
        missing_states = []
        for state in states_list:
            if state not in answered_states:
                missing_states.append(state)
        new_df = pandas.DataFrame(missing_states)
        new_df.to_csv("missing_states.csv")
    if ans_count == TOTAL_STATES:
        game_is_on = False


