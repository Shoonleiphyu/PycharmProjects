from taxi import Taxi


def main():
    taxi= Taxi("Prius 1", 100)
    taxi.drive(40)

    print(taxi)
    print(f"Current fare is $ {taxi.get_fare():.2f}\n")

    """Reset the taxi fare"""
    taxi.start_fare()

    """Print the fare after resetting"""
    print(f"Current fare is $ {taxi.get_fare():.2f} before moving.")

    distance_driven = taxi.drive(100)
    print(f"After driving another 100 km, the distance is {distance_driven} km")
    print(taxi)
    print(f"Current fare is $ {taxi.get_fare():.2f}\n")


if __name__ == '__main__':
    main()

