import time
from snake import *
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.setup(width=600, height=600)
points = 0
snake = Snake()
food=Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.t_objs[0].distance(food.f) < 15:
        scoreboard.score+=1
        food.tp()
        scoreboard.refresh()
        snake.create_t_obj()
        snake.attach()

    if snake.t_objs[0].xcor() >280 or snake.t_objs[0].xcor() <-280 or snake.t_objs[0].ycor() >280 or snake.t_objs[0].ycor() <-280 :
        game_over=True
        scoreboard.game_over()

    for t_obj in snake.t_objs[1:]:
        if t_obj.distance(snake.t_objs[0]) < 10:
            game_over = True
            scoreboard.game_over()

screen.exitonclick()
