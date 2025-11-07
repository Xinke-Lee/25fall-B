def detect(i,j,matrix,matrix2):
    N=0
    try:
        if matrix[i][j+1] == 1:
            N+=1
    except IndexError:
        pass
    try:
        if matrix[i][j-1] == 1 and j!=0:
            N+=1
    except IndexError:
        pass
    try:
        if matrix[i+1][j] == 1:
            N+=1
    except IndexError:
        pass
    try:
        if matrix[i-1][j] == 1 and i!=0:
            N+=1
    except IndexError:
        pass
    try:
        if matrix[i+1][j+1] == 1:
            N+=1
    except IndexError:
        pass
    try:
        if matrix[i+1][j-1] == 1 and j!=0:
            N+=1
    except IndexError:
        pass
    try:
        if matrix[i-1][j+1] == 1 and i!=0:
            N+=1
    except IndexError:
        pass
    try:
        if matrix[i-1][j-1] == 1 and j!=0 and i!=0:
            N+=1
    except IndexError:
        pass
    if matrix[i][j] == 1:
        if N==2 or N==3:
            matrix2[i][j] = 1
        else:
            matrix2[i][j] = 0
    if matrix[i][j]==0:
        if N==3:
            matrix2[i][j] = 1
        else:
            matrix2[i][j] = 0

n,m=map(int,input().split())
matrix=[]
matrix2=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
matrix2=[[0]*m for j in range(n)]
for i in range(n):
    for j in range(m):
        detect(i,j,matrix,matrix2)
for i in range(n):
    print(*matrix2[i])
