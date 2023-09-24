from silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Hummer", 200, 3)
    taxi.drive(20)
    print(taxi)
    print(taxi.get_fare())


if __name__ == '__main__':
    main()

