from random import randint

from car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """initialize variables adding a new var reliability"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """return the reliability of the car"""
        return f"{super().__str__()}, reliability is {self.reliability}"

    def drive(self, distance):
        """"Generate a random number between 0-100 and the reliability is greater, then drive the car
        if not distance is 0"""

    def drive(self,distance):
        random_number = randint(0, 100)
        if random_number < self.reliability:
            return super().drive(distance)
        else:
            return 0
