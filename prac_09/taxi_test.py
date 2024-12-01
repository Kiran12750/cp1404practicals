from prac_09.taxi import Taxi


def test_taxi():
    # Create a new taxi object
    my_taxi = Taxi("Prius 1", 100)  # No need to pass price_per_km since it's a class variable

    # Drive the taxi 40 km
    my_taxi.drive(40)

    # Print the taxi's details and the current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Restart the meter (start a new fare)
    my_taxi.start_fare()

    # Drive the car 100 km
    my_taxi.drive(100)

    # Print the details and the current fare after driving
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


# Call the test function
test_taxi()
