def main():
    numbers = []
    for i in range(5):
        number = float(input("Number: "))
        numbers.append(number)
    print_nums(numbers)


def print_nums(numbers):
    first_number = numbers[0]
    last_number = numbers[-1]
    smallest_number = min(numbers)
    largest_number = max(numbers)
    avg_of_num = sum(numbers) / len(numbers)
    print(f"The first number is {first_number}")
    print(f"The last number is {last_number}")
    print(f"The smallest number is {smallest_number}")
    print(f"The largest number is {largest_number}")
    print(f"The average of the numbers is {avg_of_num:.2f}")
    #print(numbers)


main()
