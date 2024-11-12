# languages.py

"""
Estimate: 15 minutes

This file will import the ProgrammingLanguage class, create objects for Python, Ruby, and Visual Basic,
and print out their details, including filtering languages with dynamic typing.

Actual time: 15 minutes.
"""

from programming_language import ProgrammingLanguage

# Create instances of ProgrammingLanguage
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Print details of the Python object
print(python)

# Create a list of the ProgrammingLanguage objects
languages = [python, ruby, visual_basic]

# Loop through and print the names of dynamically typed languages
print("\nThe dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
