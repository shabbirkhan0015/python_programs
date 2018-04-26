c=int(input("enter number of col"))
r=int(input("enter number of row"))
a=[[]*c for i in range(r)]
b=[[]*c for i in range(r)]
s=[[0]*c for i in range(r)]
d=[[0]*c for i in range(r)]
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
        s[i][j]=a[i][j]+b[i][j]
        d[i][j]=a[i][j]-b[i][j]
print("your final sum ")
print(s)
print("your final difference")
print(d)


