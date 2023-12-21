from turtle import Turtle,Screen

turtle = Turtle()
screen = Screen()
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
import pandas
answer_state = screen.textinput(title="Guess the state", prompt="What's another state name?: ")

# game_on  = True
# while game_on:
#     answer_state = screen.textinput(title="Guess the state", prompt="What's another state name?: ")

screen.mainloop()