
c=int(input("enter number of col"))
r=int(input("enter number of row"))
a=[[]*c for i in range(r)]
b=[[0]*r for i in range(c)]
for i in range(r):
    for j in range(c):
        a[i].append(int(input("enter element")))
print("your matrix is ")
print(a)
for i in range(r):
    for j in range(c):
        b[j][i]=a[i][j]

print("transpose of matrix is ")
print(b)
