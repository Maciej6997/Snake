from turtle import Turtle

#CONSTANTS VARIABLE
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0,0),(0,-20),(0,-30)]

#create class to manage snake
class Snake:

    def __init__(self):
        self.parts = []
        self.create_snake_part()
        self.head_snake = self.parts[0]



    def create_snake_part(self):
        """
        we create a third part snake at start
        start position first square is (0,0) and every square
        is 20 pixels on  the left
        """

        for position in POSITIONS:
            self.add_part(position)

    def add_part(self,place):
        snake_part = Turtle()
        snake_part.shape("square")
        snake_part.color('white')
        snake_part.penup()
        snake_part.setposition(place[0], place[1])
        self.parts.append(snake_part)

    def reset_snake(self):
        for part in self.parts:
            part.goto(1000, 1000)
        self.parts.clear()
        self.create_snake_part()
        self.head_snake = self.parts[0]

    def extend_snake(self):
        self.add_part(self.parts[-1].position())

    #
    def move(self):
        """
        Function to moving snake on th screen
        """
        for num_part in range(len(self.parts)-1, 0, -1):
            next_seg_x = self.parts[num_part - 1].xcor()
            next_seg_y = self.parts[num_part - 1].ycor()
            self.parts[num_part].goto(next_seg_x, next_seg_y)
        self.head_snake.forward(DISTANCE)

    def go_up(self):
        if self.head_snake.heading() != DOWN:
            self.head_snake.setheading(UP)

    def go_down(self):
        if self.head_snake.heading() != UP:
            self.head_snake.setheading(DOWN)

    def go_left(self):
        if self.head_snake.heading() != RIGHT:
            self.head_snake.setheading(LEFT)

    def go_right(self):
        if self.head_snake.heading() != LEFT:
            self.head_snake.setheading(RIGHT)
