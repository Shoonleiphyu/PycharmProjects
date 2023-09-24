from unreliable_car import UnreliableCar


def main():
    """testing the car"""
    good_car = UnreliableCar("Good", 100, 93)
    bad_car = UnreliableCar("Bad", 100, 6)

    print(good_car)
    print(bad_car)
    print()

    for i in range(1, 10):
        """print the distance the car drive if the random number is less than reliability"""

        print(f"Drive the car {i} km")
        print(f"{good_car.name} drive {good_car.drive(i)} km")
        print(f"{bad_car.name} drive {bad_car.drive(i)} km")


main()
