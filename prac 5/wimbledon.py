"""
Wimbledon Champions Data Processing
Estimate: 20 minutes
Actual:   15 minutes
"""

import csv

def main():
    filename = "wimbledon.csv"  # Update with your CSV file path
    data = read_wimbledon_data(filename)

    # Count champions
    champion_counts = count_champions(data)

    # Get unique countries
    countries = get_unique_countries(data)

    # Display champions and their counts
    print("Wimbledon Champions:")
    for champion, count in sorted(champion_counts.items()):
        print(f"{champion} {count}")

    # Display unique countries
    print("\nThese countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

def read_wimbledon_data(filename):
    """Read the Wimbledon data from a CSV file and return a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header row
        data = [row for row in reader]
    return data


def count_champions(data):
    """Count the number of wins for each champion and return a dictionary."""
    champion_counts = {}
    for row in data:
        champion = row[2]  # Champion is in the 3rd column
        champion_counts[champion] = champion_counts.get(champion, 0) + 1
    return champion_counts


def get_unique_countries(data):
    """Get a set of unique countries from the data."""
    countries = {row[1] for row in data}  # Country is in the 2nd column
    return countries

def read_wimbledon_data(filename):
    """Read the Wimbledon data from a CSV file and return a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header row
        data = [row for row in reader]
    return data

main()
