n=int(input("enter a  number"))
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp=temp//10
if n==sum:
    print("number is armstrong")
else:
    print("number is not armstrong")
