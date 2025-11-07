L,M=map(int,input().split())
sta=[]
A=0
for i in range(M):
    a,b=map(int,input().split())
    sta.append((a,b))
sta.sort()
for i in range(M):
    if i<M-1:
        if sta[i][1]>=sta[i+1][0]:
            sta[i+1]=(sta[i][0],max(sta[i][1],sta[i+1][1]))
            sta[i]=(0, 0)
            A+=sta[i][1]-sta[i][0]
        else:
            A+=sta[i][1]-sta[i][0]+1
    else:
        A += sta[i][1] - sta[i][0]+1
print(L-A+1)
