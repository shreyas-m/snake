from turtle import Screen
import food, score
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snake")

screen.tracer(0)

snake = Snake()
food = food.Food()
score = score.Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    snake.move()
    screen.update()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score += 1
        score.refresh()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    for segment in snake.snake_parts[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
