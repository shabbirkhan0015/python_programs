i=0
j=1
k=2
sum1=0
n=int(input("enter no.of term"))
if n<0:
    print("enter a positive number ")
elif n==1:
    print(i)
else:
    print(i)
    print(j)
    while k<n:
        sum=i+j
        print(sum)
        sum1=sum1+sum
        i=j
        j=sum
        k=k+1
print("sum of fibonacci",sum1)
