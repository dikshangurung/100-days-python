from turtle import Turtle,Screen
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard
scoreboard =Scoreboard()
snake = Snake()
screen = Screen()
food = Food()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
game_on = True;

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        scoreboard.update_score()
        snake.reset()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            scoreboard.update_score()
            snake.reset()


screen.exitonclick()






#Slicing
# vowels = ['a','e','i','o','u']
# print(vowels[2:4])
# print(vowels[::-1])











# INheritance
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#     def breathe(self):
#         print(f"Inhale exhale {self.num_eyes}")
#
# class Fish(Animal):
#     def __init__(self):
#         self.fins = "yes"
#         super().__init__()
#     def display(self):
#         print("I can breathe under water losers")
# fish = Fish()
# fish.breathe()
# print(fish.num_eyes)
