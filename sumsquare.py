def diff(n=2):
    s1=0
    sq=0
    for i in range(1,n+1):
        s1=s1+i*i
        sq=sq+i
    sq=sq**2
    return sq-s1
n=int(input("enter number"))
print(diff(n))