from turtle import Turtle


class Player:
    def __init__(self):
        self.play = Turtle()
        self.play.shape("turtle")
        self.play.penup()
        self.play.setheading(90)
        self.play.color("green")
        self.play.goto(0, -240)

    def move_up(self):
        if self.play.ycor() < 230:
            self.play.forward(30)
        else:
            pass

    def move_down(self):
        if self.play.ycor() > -230:
            self.play.backward(30)
        else:
            pass

    def move_right(self):
        if self.play.xcor() < 280:
            self.play.right(90)
            self.play.forward(30)
            self.play.left(90)
        else:
            pass

    def move_left(self):
        if self.play.xcor() > -280:
            self.play.left(90)
            self.play.forward(30)
            self.play.right(90)
        else:
            pass
