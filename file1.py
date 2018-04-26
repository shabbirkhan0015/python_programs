l=["-1","-2","4","5","6","-7","-9"]
s=' '.join(l)
count=0
print(s)
f=open("file2.txt","w")
f.write(s)
f.close()
f=open("file2.txt")
numbers=f.readline()
numbers=numbers.split()
numbers = [int(i) for i in numbers]
for i in numbers:
    if i<0:
        count=count+1
print("no of negative numbers",count)