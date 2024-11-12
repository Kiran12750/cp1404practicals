"""
Estimate: 25 minutes

The ProgrammingLanguage class will have fields to store the language's name, typing, reflection, and year.
It will include an __init__ method for initialization, an is_dynamic method to check if the language is dynamically typed,
and a __str__ method to return a formatted string.

Actual time: 30 minutes.
"""

class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """
        Initialize the ProgrammingLanguage object with name, typing, reflection, and year.
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """
        Returns True if the language is dynamically typed, otherwise False.
        """
        return self.typing == "Dynamic"

    def __str__(self):
        """
        Returns a formatted string representing the ProgrammingLanguage object.
        """
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
