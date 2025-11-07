N,M=map(int,input().split())
A=[]
for _ in range(N):
    v,w=map(int,input().split())
    A.append((v,w,v/w))
A.sort(reverse=True,key=lambda x:x[2])
value=0
weight=M
for (v,w,rate) in A:
    if w<=weight:
        weight-=w
        value+=v
    else:
        value+=rate*weight
        break
print(f"{value:.2f}")
