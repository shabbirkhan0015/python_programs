a=[1,4,9,7,8,8,23,43,56,76,98,98,12,]
b=[2,5,6,0,9,5,7,87,45,32,87,56,70,65]
mid=[]
if len(a)%2==0:
    mid.append(a[(len(a)//2)])
    mid.append (a[(len(a)//2+1)])
else:
    mid.append (a[(len(a)//2)])
if len(b)%2==0:
    mid.append(b[(len(a)//2)])
    mid.append (b[(len(a)//2+1)])
else:
    mid.append (b[(len(a)//2)])
print("1st list is")
print(a)
print("2nd list is ")
print(b)
print("the final list is")
print(mid)
