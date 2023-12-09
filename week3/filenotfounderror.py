try:
    filename= input("Enter file: ")
    in_file=open(filename)
    text= in_file.read()
    in_file.close()
    print(text)
except FileNotFoundError:
    print("File not found!!!")


# type error only accept string input
# # zero division error
# # name error
# # value error