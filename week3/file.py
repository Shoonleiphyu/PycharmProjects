### name file ###
file_name = input("Enter file name: ")
out_file = open(file_name, 'w')

name = input("Enter your name: ")
f = open(file_name, "a")
f.writelines(name)
f.close()

f = open(file_name, "r")
print("Your name is", f.read())
print()
## sum of two numbers ##
number_file = "number.txt"
in_file = open(number_file)
numbers = in_file.readlines()
in_file.close()

if len(numbers) >= 2:
    num1 = int(numbers[0])
    num2 = int(numbers[1])
    result = num1 + num2
    print("The result of adding the first two numbers is:", result)
else:
    print("The file doesn't contain enough numbers.")

def calculate_total(number_file):
    total = 0

    in_file = open(number_file)
    for line in in_file:
        try:
            number = int(line.strip())
            total += number
        except ValueError:
            print(f"Skipping line: '{line.strip()}' as it is not a valid integer.")
    in_file.close()
    return total
print()
##total##
number_file = "number.txt"
total_result = calculate_total(number_file)
print("The total of all numbers in the file is:", total_result)
