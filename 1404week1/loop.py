for i in range(0, 4):
    for j in range(0, i+1):
        print("*", end='')
    print()

for i in range(0,6):
    for j in range (0, i):
        print (" ", end = '')
    for k in range(0, 6-i):
        print("*", end ='')
    print ()

for i in range(0,6):
    for j in range (0, 5-i):
        print (" ", end = '')
    for k in range(0, i+1):
        print("*", end ='')
    print ()

for i in range(0,6):
    for j in range (0, 6-i):
        print ("*", end = '')

    print ()