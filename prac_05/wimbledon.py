import csv


def main():
    filename = "wimbledon.csv"
    data = read_csv_file(filename)
    champion_counts = calculate_champion_counts(data)
    display_champion_counts(champion_counts)
    countries = get_countries(data)
    display_countries(countries)


def read_csv_file(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        csv_reader = csv.reader(in_file)
        next(csv_reader)
        for row in csv_reader:
            data.append(row)
    return data


def calculate_champion_counts(data):
    champion_counts = {}
    for row in data:
        champion = row[2]
        if champion in champion_counts:
            champion_counts[champion] += 1
        else:
            champion_counts[champion] = 1
    return champion_counts


def display_champion_counts(champion_counts):
    print("Wimbledon Champions:")
    for country, count in champion_counts.items():
        print(f"{country} {count}")


def get_countries(data):
    countries = set()
    for row in data:
        countries.add(row[2])
    return countries


def display_countries(countries):
    sorted_countries = sorted(countries)
    countries_string = ", ".join(sorted_countries)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(countries_string)



main()
