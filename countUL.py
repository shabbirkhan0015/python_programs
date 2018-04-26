def count(s): 
    u=0
    l=0
    for i in s:
        if ord(i)>64 and ord(i)<92:
            u=u+1
    
        elif ord(i)>96 and ord(i)<123:
            l=l+1
    print("no. of lowercase",l)
    print("no. of uppercase",u)
            
s=input("enter your string")
print(count(s))