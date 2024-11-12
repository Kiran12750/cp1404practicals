"""
Module: guitar.py

Estimate: 1 hour
Actual: 45 minutes

This module defines the Guitar class which includes attributes for the name,
year, and cost of a guitar, along with methods to:
1. Initialize the guitar with name, year, and cost.
2. Provide a string representation of the guitar.
3. Calculate the age of the guitar.
4. Determine if the guitar is vintage (50 or more years old).

"""

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initializes the guitar with name, year, and cost"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns a string representation of the guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year):
        """Returns the age of the guitar as the difference between the current year and the guitar's year"""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Returns True if the guitar is 50 or more years old, False otherwise"""
        return self.get_age(current_year) >= 50
