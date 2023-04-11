from turtle import Turtle

##class Paddle:
##    def __init__(self, position):
##        self.paddle = Turtle(shape='square')
##        self.paddle.penup()
##        self.paddle.color('white')
##        self.paddle.setheading(90)
##        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
##        self.paddle.goto(position)
##
##    def move_upward(self):
##        #self.paddle.forward(20)
##        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor()+20)
##
##    def move_downward(self):
##        #self.paddle.forward(-20)
##        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor()-20)

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)

    def move_upward(self):
        self.forward(20)
##        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor()+20)

    def move_downward(self):
        self.forward(-20)
##        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor()-20)
