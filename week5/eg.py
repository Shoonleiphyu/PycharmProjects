def main():
    filename = "wimbledon.csv"
    data = read_csv_file(filename)

    champions = count_champions(data)
    sorted_champions = sorted(champions.items(), key=lambda x: x[0])

    print("Wimbledon Champions:")
    for champion, wins in sorted_champions:
        print(f"{champion} {wins}")

    countries = get_countries(data)
    countries_string = ', '.join(countries)
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(countries_string)


def get_countries(data):
    countries = set()
    for row in data:
        country = row[1]
        if country != "Country":
            countries.add(country)
    sorted_countries = sorted(countries)
    return sorted_countries


def count_champions(data):
    champions = {}
    for row in data:
        champion_name = row[2]

        if champion_name in champions:
            champions[champion_name] += 1
        else:
            champions[champion_name] = 1
    return champions


def read_csv_file(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            line = line.strip()
            if line:
                row = line.split(',')
                data.append(row)
    return data


main()