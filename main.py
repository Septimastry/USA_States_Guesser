import turtle
import pandas

screen= turtle.Screen()
screen.title("U.S. States Guesser")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_is_on = True
ans_count = 0
TOTAL_STATES = 50


#create dataframe
df = pandas.read_csv("50_states.csv")
states = df.state
#main loop
while game_is_on:
    if ans_count ==0:
        answer_state = screen.textinput("Guess the state", "What's another state's name?")
    else:
        answer_state = screen.textinput(f"{ans_count}/{TOTAL_STATES} States Correct", "What's another state's name?")
        edited_ans = answer_state.upper()
        for state in states:
            if edited_ans == state:
                ans_count+=1
                y = turtle.Turtle()
                y.penup()
                y.goto(df[states==state].x, df[states==state].y)







turtle.mainloop()
