N,D=map(int,input().split())
Ai=list(map(int,input().split()))
Ai.sort()
delta=[]
for i in range(0,2*N,2):
    delta.append(Ai[i+1]-Ai[i])
if max(delta)>D:
    print("No")
else:
    print("Yes")