# name= input("name: ") # give the newfile a name
# out_file=open("name.txt", "w") # writing a new file
# print(name, file=out_file)
# out_file.close()
# print()


out_file=open("name.txt", "w") # open file and start writing
out_file.writelines(["this is ", "my name"]) # write lines
out_file.close()

out_file=open("name.txt", "r") # read back
print(out_file.read())
print()

name=input("enter something: ")
f=open("name.txt", "a") # open file and start writing
f.writelines(name) # write lines
f.close()

f=open("name.txt", "r") # read back
print(f.read())