n,m=map(int,input().split())
maps=[]
for i in range(n):
    a=list(map(int,input().split()))
    maps.append(a)
length=0
for i in range(n):
    for j in range(m):
        if maps[i][j]==1:
            try:
                if maps[i+1][j]==0:
                    length+=1
            except IndexError:
                length+=1
            try:
                if maps[i][j+1]==0:
                    length+=1
            except IndexError:
                length+=1
            if maps[i][j-1]==0 or j-1<0:
                length+=1
            if maps[i-1][j]==0 or i-1<0:
                length+=1
print(length)
