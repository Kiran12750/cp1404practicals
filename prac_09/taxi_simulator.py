from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def print_menu():
    """Print the menu options."""
    print("q)uit, c)hoose taxi, d)rive")

def display_taxis(taxis):
    """Display a list of taxis available for selection."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def choose_taxi(taxis):
    """Allow user to choose a taxi from the list."""
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid input")
        return None

def taxi_simulator():
    """Main function to run the taxi simulator."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0.0

    while True:
        print_menu()
        choice = input(">>> ").lower()

        if choice == "q":
            # Quit the program and print the final total bill and status of taxis
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            break

        elif choice == "c":
            # Choose a taxi
            display_taxis(taxis)
            current_taxi = choose_taxi(taxis)

            if current_taxi is None:
                print(f"Bill to date: ${total_bill:.2f}")
                continue

            print(f"Bill to date: ${total_bill:.2f}")

        elif choice == "d":
            if current_taxi is None:
                # If no taxi has been chosen, remind the user to choose one
                print("You need to choose a taxi before you can drive")
                print(f"Bill to date: ${total_bill:.2f}")
                continue

            # Drive the chosen taxi
            try:
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)

                # Calculate fare and update the bill
                fare = current_taxi.get_fare()
                total_bill += fare
                print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                print(f"Bill to date: ${total_bill:.2f}")
            except ValueError:
                print("Invalid distance")
                print(f"Bill to date: ${total_bill:.2f}")
        else:
            print("Invalid option")
            print(f"Bill to date: ${total_bill:.2f}")

if __name__ == "__main__":
    taxi_simulator()
