import random
from prac_09.unreliable_car import UnreliableCar


def test_unreliable_car():
    reliability = 30  # Set reliability to 30% for the test
    my_car = UnreliableCar("Unreliable", 100, reliability)

    # Perform the test multiple times (e.g., 100 times) to check reliability
    drive_count = 0
    total_attempts = 100

    for _ in range(total_attempts):
        distance = my_car.drive(10)  # Attempt to drive 10 km
        if distance > 0:
            drive_count += 1  # Count how many times the car drives

    # Print the results of the test
    print(f"Out of {total_attempts} attempts, the car drove {drive_count} times.")

    # You can check if the number of successful drives is approximately equal to the reliability percentage
    print(f"Expected range: {total_attempts * (reliability / 100) - 5} to {total_attempts * (reliability / 100) + 5}")
    print(f"Actual drives: {drive_count}")


# Call the test function
test_unreliable_car()
