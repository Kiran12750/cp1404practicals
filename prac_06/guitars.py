"""
Module: guitars.py

Estimate: 1 hour
Actual: 1 hour 10 minutes

This module allows the user to input details for multiple guitars, stores them in a list,
and then prints a summary of the guitars, including whether they are vintage. The program
continues to prompt the user for guitar details until an empty name is entered.

"""

from guitar import Guitar

def main():
    """Guitar program, using Guitar class."""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:  # lists, strings and other collections are False when empty, True when non-empty
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            # Note the use of the format method and numbered placeholders
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i, guitar, vintage_string))
    else:
        print("No guitars :( Quick, go and buy one!")
# Running the program
main()
