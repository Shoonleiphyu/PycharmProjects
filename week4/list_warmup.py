numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0]    3 # index 0
# numbers[-1]   2 # index -1
# numbers[3]    1 # index 3
# numbers[:-1]  [3, 1, 4, 1, 5, 9] + index -1 excluded
# numbers[3:4]  [1] # start from index 3 and 4 excluded
# 5 in numbers  true # find 5 in numbers
# 7 in numbers  false # find 7 in numbers
# "3" in numbers    false (:string not int)
# numbers + [6, 5, 3]      [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] # add to the last

print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])

numbers[0]= "ten"
numbers[-1]= 1
print(numbers)

print(numbers[2:]) # first 2 indexes excluded

print(9 in numbers)