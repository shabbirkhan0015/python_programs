list=[1,4,6,7,8]
n=int(input("enter no of rotation you want to perform  "))
while n>0:
    temp=list[0]
    for i in range (len(list)-1):
        list[i]=list[i+1]
    list[i+1]=temp
    n=n-1
print("final list is ")
print(list)