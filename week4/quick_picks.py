import random

min_num = 1
max_num = 45
num_numbers = 6


def main():
    num_quick_picks = int(input("How many quick picks? "))
    for i in range(num_quick_picks):
        quick_pick = generate_quick_picks()
        print(" ".join(str(number) for number in quick_pick))


def generate_quick_picks():
    numbers = set()  # list
    while len(numbers) < numbers:
        number = random.randint(min_num, max_num)
        numbers.add(number)
    return sorted(numbers)


main()

