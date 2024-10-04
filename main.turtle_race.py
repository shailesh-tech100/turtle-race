import turtle
from turtle import Turtle,Screen
import random
colors=["red","orange","yellow","green","blue","purple"]
y_position=[-100,-60,-20,20,60,100]
is_race_on=False
all_turtle=[]

screen = Screen()
user_bet=screen.textinput("make your bet","which turtle wll win the race? Enter a color: ")



for color in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[color])
    new_turtle.penup()
    new_turtle.goto(x=-320, y=y_position[color])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtles in all_turtle:
        if turtles.xcor() > 300:
            is_race_on = False
            winning_color=turtles.pencolor()
            if winning_color == user_bet:
                print(f"you win! The {winning_color} turtle win the race")
            else:
                print(f"you lost! The {winning_color} turtle win the race")

        random_distance=random.randint(0,10)
        turtles.forward(random_distance)



screen.exitonclick()