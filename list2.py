x=[]
b=[]
n=int(input("enter number of elements"))
for i in range(0,n):
    item=int(input("enter element "))
    x.append(item)
for i in range(0,n):
    if x[i]==3:
        b.append(3)
for j in range(0,n):
    if x[j]==1:
        b.append(1)
for k in range(0,n):
    if x[k]==4:
        b.append(4)
if b[0]==3 and b[1]==1 and b[2]==4:
    print(b)
    
else:
    print("all elements not found")
        

