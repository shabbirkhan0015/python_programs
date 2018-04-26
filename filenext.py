def sub_in_file(filename,s):
    count=0
    f=open(filename)
    for line in f:
        if s in line:
            count=count+1
    return count
filename = input("Enter the name of file:")
f= open(filename,"w")
f.write("this is my house this is my room")
f.close()
s=input("enter substring ")
c=sub_in_file(filename,s)
print(c)