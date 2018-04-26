a={}
l=[-1,-2,3,5,6]
s=' '.join(l)
count=0
print(s)
f=open("file2.txt","w")
f.write(s)
f.close()
f=open("file2.txt")
numbers=f.read()
cols, rows = (int(val) for val in numbers[0].split())
for number in numbers:
    print(number)
    if number<-1:
        count=count+1