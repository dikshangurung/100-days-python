from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
class Snake:
    def __init__(self):
        self.positions = [(0,0),(-20,0),(-40,0)]
        self.segments = []
        self.find_pos()
        self.head = self.segments[0]
        #THis is so that every time we make a constructor the function gets call out
    def find_pos(self):
        for position in self.positions:
            self.make_snake(position)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.find_pos()
        self.head = self.segments[0]

    def make_snake(self,position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)
    def extend(self):
        self.make_snake(self.segments[-1].position())
    def move(self):
        for el in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[el - 1].xcor()
            new_y = self.segments[el - 1].ycor()
            self.segments[el].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)



    # def add_snake(self):
    #     self.segments.append(new_turtle)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        # self.segments[0].forward(MOVE_DISTANCE)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)