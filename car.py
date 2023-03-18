from turtle import Turtle
import random
COLOR = ["green", "yellow", "purple", "gray", "red", "orange", "pink", "blue"]
CARS_POSITIONS = [(-580, -205), (-410, -175), (-380, -145), (-620, -115), (-430, -85), (-690, -55), (-540, -25),
                  (-450, 5), (-500, 35), (-510, 65), (-490, 95), (-510, 125), (-550, 155), (-390, 185), (-630, 215)]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.fast = 2
        self.hideturtle()
        self.car = Turtle("square")
        self.car.penup()
        self.car.shapesize(1, 2)
        self.car.color(random.choice(COLOR))
        self.car.goto(random.choice(CARS_POSITIONS))

    def cars_location(self):
        self.car.forward(self.fast)
        if self.car.xcor() >= 380:
            self.car.goto(random.choice(CARS_POSITIONS))
            self.car.color(random.choice(COLOR))

    def speed_fast(self):
        self.fast += 1
