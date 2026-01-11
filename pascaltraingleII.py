rowIndex=3
triangle=[]
for i in range(rowIndex+1):
    col=i+1
    l=[]
    for j in range(col):
        if j==0 or j==col-1:
            l.append(1)
        else :
            l.append(triangle[i-1][j-1]+triangle[i-1][j])
    triangle.append(l)
print(triangle[rowIndex])