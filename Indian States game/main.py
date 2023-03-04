import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. STATES GAME")
image ="blankmap.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states =[]

while len(guessed_states) < 29:
    data = pandas.read_csv("indian_states_data.csv")
    all_states = data.state.to_list()


    answer_state = screen.textinput(title = f"{len(guessed_states)}/28 States Correct",
                                    prompt="Guess a state's  name").title()
    if answer_state == "Exit":
        missing_states =[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break


    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())

turtle.mainloop()