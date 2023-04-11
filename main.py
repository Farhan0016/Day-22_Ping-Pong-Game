# TODO 1: Create the screen
# TODO 2: Create and move a paddle
# TODO 3: Create another paddle
# TODO 4: Create the ball and make it move
# TODO 5: Detect collision with wall and bounce
# TODO 6: Detect collision with paddle
# TODO 7: Detect when paddle misses
# TODO 8: Keep Score

from time import sleep
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.title('Ping Pong')
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

screen.onkey(left_paddle.move_upward, 'w')
screen.onkey(left_paddle.move_downward, 's')
screen.onkey(right_paddle.move_upward, 'Up')
screen.onkey(right_paddle.move_downward, 'Down')

while True:
    screen.update()
    sleep(0.1)
    ball.move()

    # Detect ball collision with upper and lower wall
    x_coordinate = ball.xcor()
    y_coordinate = ball.ycor()
    if y_coordinate > 280 or y_coordinate < -280:
        # ball.setheading(ball.heading() + 45)
        # ball.setheading(ball.heading() * -1)
        ball.wall_bounce()

    # Detect ball collision with paddle

    # if ball.distance(left_paddle) <= 20 or ball.distance(right_paddle) <= 20:
    #   ball.setheading(ball.heading() * -1)
    if (ball.distance(right_paddle) < 50 and ball.xcor() == 340) or (
            ball.distance(left_paddle) < 50 and ball.xcor() == -340):
        ball.paddle_bounce()

    # Detect if right paddle miss the ball
    if ball.xcor() >= 380:
        scoreboard.update_score_l()
        ball.reset_position()
    # Detect if left paddle miss the ball
    elif ball.xcor() <= -380:
        scoreboard.update_score_r()
        ball.reset_position()

screen.exitonclick()
