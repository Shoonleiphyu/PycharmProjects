FILENAME = "subject_data.txt"
def main():
    data = get_data()
    print(data)
    print()
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data=[]
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        data.append(parts) # append parts
        print("----------")
    input_file.close()
    return data # return the appended data


def display_subject_details(data):
    """Display subject details like: CP1401 is taught by Ada Lovelace and has 192 students."""
    for subject_details in data:
        subject_code, lecturer, num_students = subject_details
        print(f"{subject_code} is taught by {lecturer} and has {num_students} students")


main()
