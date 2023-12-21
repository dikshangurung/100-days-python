import random
names = ["Dikshan","Kushal","Sakar","Satya","Karki"]
student_scores = {name:random.randint(1,100) for name in names}
passes_student = {student:score for (student,score) in student_scores.items() if score>40}
print(student_scores)
print(passes_student)

# import pandas
# from turtle import Turtle,Screen
# turtle_display = Turtle()
# screen = Screen()
# image = "./blank_states_img.gif"
# screen.addshape(image)
# turtle_display.shape(image)
# data_frame = pandas.read_csv("50_states.csv")
# data_list = data_frame["state"].to_list()
# states_number = 50
# correct_answer = 0
# correct_list = []
# learning_list = []
# while correct_answer <= 50:
#     answer = screen.textinput(title=f"{correct_answer}/{states_number}",
#                               prompt="What is the name of next state? ").title()
#
#     if answer == "Exit":
#         learning_list = [state for state in data_list if state not in correct_list]
#         data_learn = {
#             "state" : learning_list
#         }
#         data = pandas.DataFrame(data_learn)
#         data.to_csv("learn.csv")
#         break
#     if answer in data_list:
#         state_data_row = data_frame[data_frame.state == answer]
#         check_list_x = int(state_data_row["x"])
#         check_list_y = int(state_data_row["y"])
#         turtle_text = Turtle()
#         turtle_text.hideturtle()
#         turtle_text.penup()
#         turtle_text.goto(check_list_x, check_list_y)
#         turtle_text.write(answer)
#         correct_answer += 1
#         correct_list.append(answer)
# while correct_answer <= 50:
#     answer = screen.textinput(title=f"{correct_answer}/{states_number}",prompt="What is the name of next state? ").title()
#     check = data_frame[data_frame.state == answer]
#     check_bool = len(check)
#     if check_bool == 1:
#         check_list_x = int(check["x"])
#         check_list_y = int(check["y"])
#         turtle_text = Turtle()
#         turtle_text.hideturtle()
#         turtle_text.penup()
#         turtle_text.goto(check_list_x,check_list_y)
#         turtle_text.write(answer)

# import turtle
# import pandas
#
# screen = turtle.Screen()
# screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
#
# data = pandas.read_csv("50_states.csv")
# all_states = data.state.to_list()
# print(all_states)
# guessed_states = []
#
# while len(guessed_states) < 50:
#     answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
#                                     prompt="What's another state's name?").title()
#     if answer_state == "Exit":
#         missing_states = []
#         for state in all_states:
#             if state not in guessed_states:
#                 missing_states.append(state)
#         new_data = pandas.DataFrame(missing_states)
#         new_data.to_csv("states_to_learn.csv")
#         break
#     if answer_state in all_states:
#         guessed_states.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(int(state_data.x), int(state_data.y))
#         t.write(answer_state)
