from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Write a program of taxi simulator which uses Taxi and SilverServiceTaxi Classes.
    Each time, until they quit:
    The user should be able to choose from a list of available taxis,
    They can choose how far they want to drive,
    At the end of each trip, show them the trip cost and add it to their bill."""
    total_fare = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>>").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                # error checking
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far?"))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} costs you {trip_cost:.2f}")
                total_fare += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(MENU)
        menu_choice = input(">>> ").lower()

    print(f"Bill to date: ${total_fare:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Displaying the number list of taxis"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()

