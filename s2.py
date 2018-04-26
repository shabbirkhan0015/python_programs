m=[[]*3 for i in range(3)]
l=[]
for i in range(3):
    for j in range(3):
        x=int(input("enter an element"))
        m[i].append(x)
        
print(m)

for i in range(3):
    l.append(max(m[i]))
print("largest element" )
print(max(l))
print("smallest element" )
print(min(l))