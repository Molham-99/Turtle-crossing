from turtle import Turtle, Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
screen = Screen()
screen.listen()
screen.tracer(0)
player = Player()
score = Scoreboard()
car = Car()
car1 = Car()
car2 = Car()
car3 = Car()
car4 = Car()
car5 = Car()
car6 = Car()
car7 = Car()
car8 = Car()
car9 = Car()
car10 = Car()
screen.bgcolor("white")
screen.screensize(600, 600)
screen.title("Turtle Crossing Game Created by Molham")
line_position = -220
for line in range(0, 16):
    line = Turtle()
    line.pensize(2)
    line.penup()
    line.hideturtle()
    line.goto(-320, line_position)
    for x in range(0, 32):
        line.pendown()
        line.forward(10)
        line.penup()
        line.forward(10)
    line_position += 30
screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_down, key="Down")
screen.onkey(fun=player.move_right, key="Right")
screen.onkey(fun=player.move_left, key="Left")
game_is_on = True
while game_is_on:
    screen.update()
    score.scores()
    car.cars_location()
    car1.cars_location()
    car2.cars_location()
    car3.cars_location()
    car4.cars_location()
    car5.cars_location()
    car6.cars_location()
    car7.cars_location()
    car8.cars_location()
    car9.cars_location()
    car10.cars_location()
    if player.play.ycor() > 210:
        score.score_increase()
        player.play.goto(0, -240)
        car.speed_fast()
        car1.speed_fast()
        car2.speed_fast()
        car3.speed_fast()
        car4.speed_fast()
        car5.speed_fast()
        car6.speed_fast()
        car7.speed_fast()
        car8.speed_fast()
        car9.speed_fast()
        car10.speed_fast()
    if player.play.distance(car.car) < 25 or player.play.distance(car1.car) < 25 or player.play.distance(car2.car) < 25\
            or player.play.distance(car3.car) < 25 or player.play.distance(car4.car) < 25 or\
            player.play.distance(car5.car) < 25 or player.play.distance(car6.car) < 25 or \
            player.play.distance(car7.car) < 25 or player.play.distance(car8.car) < 25 \
            or player.play.distance(car9.car) < 25 or player.play.distance(car10.car) < 25:
        game_is_on = False
        score.game_over()
        screen.update()
screen.exitonclick()
