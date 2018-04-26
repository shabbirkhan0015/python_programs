s=[]
def add(l1,l2):
    s=[[0]*2 for i in range(3)]
    for i in  range(0,len(l1)):
        for j in range(0,len(l1[i])):
            s=s+s[i][j]
        return(s)


print(add([[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]))

        