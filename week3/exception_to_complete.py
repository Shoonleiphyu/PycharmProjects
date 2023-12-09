is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished=True # to exit the loop
    except ValueError: # catch the value error
        print("Please enter a valid integer.")
print("Valid result is:", result)