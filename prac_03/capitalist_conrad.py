import random

# Constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = 'stock_prices.txt'

# Set up the initial price and the number of days
price = INITIAL_PRICE
number_of_days = 0

# Open the output file for writing
with open(FILENAME, 'w') as out_file:
    print(f"Starting price: ${price:,.2f}", file=out_file)

    while MIN_PRICE <= price <= MAX_PRICE:
        number_of_days += 1
        price_change = 0

        # Generate a random integer of 1 or 2
        # If it's 1, the price increases; otherwise, it decreases
        if random.randint(1, 2) == 1:
            # Generate a random floating-point number between 0 and MAX_INCREASE
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            # Generate a random floating-point number between -MAX_DECREASE and 0
            price_change = random.uniform(-MAX_DECREASE, 0)

        # Update the price
        price *= (1 + price_change)

        # Print the price to the file
        print(f"On day {number_of_days}, price is: ${price:,.2f}", file=out_file)

    # Print a final message when the simulation ends
    print(f"Simulation ended after {number_of_days} days.", file=out_file)
