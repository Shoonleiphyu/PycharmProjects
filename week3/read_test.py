filename="test_text"
in_file=open(filename)
text=in_file.read()
in_file.close()
print(text)
print()

filename="test_text"
in_file=open(filename)
for line in in_file:
    text=in_file.read()
in_file.close()
print(text)
print()

filename="test_text"
in_file=open(filename)
text=in_file.readline()
in_file.close()
print(text)
print()

filename="test_text"
in_file=open(filename)
text=in_file.readlines()
in_file.close()
print(text)

# use split() and it will store in a list
# access the words by list index
