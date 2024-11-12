from prac_06.car import Car

def main():
    """Demo test code to show how to use car class."""
    # Create a new car object called "limo" with 100 units of fuel
    limo = Car("Limo", 100)

    # Add 20 more units of fuel to the limo
    limo.add_fuel(20)

    # Print the amount of fuel in the limo
    print(f"Fuel in limo: {limo.fuel}")

    # Attempt to drive the limo 115 km
    distance_driven = limo.drive(115)
    print(f"Distance driven: {distance_driven} km")

    # Print the limo's details using the __str__ method
    print(limo)

main()
