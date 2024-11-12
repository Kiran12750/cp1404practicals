"""
Module: guitar_test.py

Estimate: 30 minutes
Actual: 20 minutes

This module tests the Guitar class to verify that the `get_age` and `is_vintage`
methods function as expected. The tests include comparing the expected age and
vintage status with the actual results.

"""

from guitar import Guitar

def test_guitar():
    # Creating test guitars
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 765.4)

    # Test get_age() and is_vintage() methods
    print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age(2022)}")
    print(f"{guitar2.name} get_age() - Expected 9. Got {guitar2.get_age(2022)}")

    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage(2022)}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage(2022)}")

# Running the tests
test_guitar()
