import csv
from guitar import Guitar

def main():
    filename = 'guitars.csv'

    # Read the guitars from the CSV file
    guitars = read_guitars(filename)

    # Display all guitars
    print("Current guitars:")
    display_guitars(guitars)

    # Sort guitars by year
    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    # Ask if the user wants to add a guitar
    add_new = input("\nDo you want to add a new guitar? (y/n): ").lower()
    if add_new == 'y':
        # Add guitars until the user opts to stop
        add_more = 'y'
        while add_more == 'y':
            guitar = add_guitar()
            guitars.append(guitar)
            # Ask if the user wants to add another guitar
            add_more = input("\nDo you want to add another guitar? (y/n): ").lower()


def read_guitars(filename):
    """Reads guitars from the given CSV file and returns a list of Guitar objects."""
    guitars = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                name, year, cost = row
                guitar = Guitar(name, int(year), float(cost))
                guitars.append(guitar)
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list of guitars.")
    return guitars


def save_guitars(filename, guitars):
    """Saves a list of Guitar objects to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def display_guitars(guitars):
    """Displays a list of guitars."""
    for guitar in guitars:
        print(guitar)


def add_guitar():
    """Prompts the user to enter details of a new guitar and returns a Guitar object."""
    name = input("Enter the guitar name: ")
    year = int(input("Enter the year of the guitar: "))
    cost = float(input("Enter the cost of the guitar: "))
    return Guitar(name, year, cost)


    # Save the updated list of guitars back to the file
    save_guitars(filename, guitars)
    print("\nGuitars saved to the file.")


if __name__ == "__main__":
    main()
