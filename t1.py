def rev(fi1e,string):
    s1 = string.split()
    s3 = s1.reverse()
    file.write(s3)
    
file = open("file.txt",'w')
rev(file,"hello")
file.close()
