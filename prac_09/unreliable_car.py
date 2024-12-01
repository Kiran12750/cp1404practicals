import random
from prac_09.car import Car


class UnreliableCar(Car):
    """A Car that may or may not drive based on reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on the parent Car."""
        super().__init__(name, fuel)
        self.reliability = reliability  # Set the reliability attribute

    def drive(self, distance):
        """Drive the car, but only if a random number is less than reliability."""
        random_chance = random.randint(0, 100)  # Generate a random number between 0 and 100
        if random_chance < self.reliability:
            # If the random number is less than reliability, drive the car
            return super().drive(distance)  # Calls the parent's drive method
        else:
            # If not, the car does not drive and returns 0 km
            return 0
