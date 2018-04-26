num = int(input("Enter an number  "))
for i in range(1, num + 1):
    for j in range(num -  i,  0,  -1):
        print(" "),
    for j in range(i, 0, -1):
        print(j),
    for j in range(2, i + 1):
        print(j),
    print("") 
