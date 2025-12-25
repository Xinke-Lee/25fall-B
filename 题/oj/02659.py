A,B,K=map(int,input().split())
matrix=[[0]*B for _ in range(A)]
nums_True=0
for _ in range(K):
    R,S,P,T=map(int,input().split())
    r=int((P-1)/2)
    if T==0:
        for i in range(-r,r+1):
            for j in range(-r,r+1):
                if 0<=R+i-1<A and 0<=S+j-1<B:
                    matrix[R-1+i][S-1+j]=-1e9
    else:
        nums_True+=1
        for i in range(-r,r+1):
            for j in range(-r,r+1):
                if 0<=R+i-1<A and 0<=S+j-1<B:
                    matrix[R-1+i][S-1+j]+=1
nums=0
for b in matrix:
    for i in b:
        if i==nums_True:
            nums+=1
print(nums)