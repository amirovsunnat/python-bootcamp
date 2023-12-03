import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "blue", "purple", "grey"]
STARTING_MOVING_DISTANCE = 5
MOVE_INCREMENT = 1


class Car:
    """Car class."""
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVING_DISTANCE

    def create_car(self):
        """Creates new car."""
        # we generate random number from 1 to 6
        number = random.randint(1, 6)
        # if number is 1 then we continue creating a new car
        if number == 1:
            car = Turtle("square")
            car.turtlesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(x=400, y=random.randint(-270, 250))
            self.all_cars.append(car)

    def move_cars(self):
        """Move cars in the all_cars."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_up(self):
        """Increase car speed."""
        self.car_speed += MOVE_INCREMENT
