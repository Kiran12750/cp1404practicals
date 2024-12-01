import random

# Line 1: Generates a random integer between 5 and 20, inclusive.
print(random.randint(5, 20))  # line 1
# What did you see on line 1?
# This will display a random integer value between 5 and 20.
# What was the smallest number you could have seen, what was the largest?
# Smallest: 5, Largest: 20

# Line 2: Generates a random number from 3 to 10 with a step of 2.
print(random.randrange(3, 10, 2))  # line 2
# What did you see on line 2?
# This will display either 3, 5, 7, or 9.
# What was the smallest number you could have seen, what was the largest?
# Smallest: 3, Largest: 9
# Could line 2 have produced a 4?
# No, line 2 cannot produce a 4 since it only returns odd numbers.

# Line 3: Generates a random floating-point number between 2.5 and 5.5.
print(random.uniform(2.5, 5.5))  # line 3
# What did you see on line 3?
# This will display a random float value between 2.5 and 5.5.
# What was the smallest number you could have seen, what was the largest?
# Smallest: 2.5, Largest: 5.5

# Code to produce a random number between 1 and 100 inclusive.
random_number = random.randint(1, 100)
print(random_number)
