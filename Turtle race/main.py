from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="Make your bet",prompt="which turtle will win the race?")
y_pos = [-100,-50,0,50,100]
colors = ["orange", "red", "yellow", "blue" ,"purple"]
all_turtles =[]


for turtle_index in range(0,5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_pos[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        speed = random.randint(0, 10)
        turtle.forward(speed)

screen.exitonclick()