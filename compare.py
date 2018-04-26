c=int(input("enter number of col"))
r=int(input("enter number of row"))
a=[[]*c for i in range(r)]
b=[[]*c for i in range(r)]
for i in range(r):
    for j in range(c):
        a[i].append(int(input("enter element")))
print("your matrix is ")
print(a)
for i in range(r):
    for j in range(c):
        b[i].append(int(input("enter element")))
print("your matrix is ")
print(b)
for i in range(r):
    for j in range(c):
        if(a[i][j]==b[i][j]):
            flag=1
        else:
            flag=0
if flag==1:
    print("equal matrix")
else:
    print("not equal")