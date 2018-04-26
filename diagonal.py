s=0
c=int(input("enter number of col"))
r=int(input("enter number of row"))
a=[[]*c for i in range(r)]

for i in range(r):
    for j in range(c):
        a[i].append(int(input("enter element")))
print(a)
for i in range(r):
    s=s+a[i][i]
print(s)