password=input("Enter password: ")
num_of_asterisk= len(password)

while num_of_asterisk <=0:
    print("no password entered")
    password = input("Enter password: ")
    num_of_asterisk = len(password)
#for i in range(num_of_asterisk):
    #print("*", end="")
print(num_of_asterisk* "*")






