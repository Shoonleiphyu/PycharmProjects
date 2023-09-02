import csv

from guitar import Guitar


def read_guitars():
    guitars = []
    file = open('guitars.csv', 'r')
    reader = csv.reader(file)

    for line in reader:
        name, year, cost = line
        year = int(year)
        cost = float(cost)
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
    file.close()
    return guitars


def display_guitars(guitars):
    if not guitars:
        print("No guitars found.")
    else:
        for i, guitar in enumerate(guitars, 1):
            print(f"Guitar {i}: {guitar}")


def add_new_guitar():
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    return Guitar(name, year, cost)


def write_guitars(guitars):
    with open('guitars.csv', 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost:.2f}\n")


def sort_guitars_years(guitars):
    guitars.sort()


def main():
    guitars = read_guitars()
    sort_guitars_years(guitars)
    display_guitars(guitars)

    new_guitar = add_new_guitar()
    guitars.append(new_guitar)
    write_guitars(guitars)

    sort_guitars_years(guitars)
    print("\nThese are my guitars:")
    display_guitars(guitars)


main()
