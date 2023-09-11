# imports packagaes
import time
from turtle import Screen
from Snake import Snake
from food import Food
from Score import Score

# create and configure screen options
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

if __name__ == "__main__":

    # create snake
    snake = Snake()
    food = Food()
    score = Score()

    screen.update()
    screen.listen()
    # import wsad control from Snake class
    screen.onkey(snake.go_up, 'w')
    screen.onkey(snake.go_down, 's')
    screen.onkey(snake.go_right, 'd')
    screen.onkey(snake.go_left, 'a')

    # variable to manage game
    game_on = True
    # loop to game
    while game_on:
        time.sleep(.2)
        snake.move()
        screen.update()

        # collision detection with food
        if snake.head_snake.distance(food) < 15:
            food.refresh()
            snake.extend_snake()
            score.reset_turtle()
            score.update_score()

        # collision with wall
        if abs(snake.head_snake.xcor()) > 280 or abs(snake.head_snake.ycor()) > 280:
            score.reset_score()
            snake.reset_snake()

        # collision with tail
        for i in range(1, len(snake.parts)):
            if snake.head_snake.distance(snake.parts[i]) < 10:
                score.reset_score()
                snake.reset_snake()


    # end program
    screen.exitonclick()
