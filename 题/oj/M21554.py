n=int(input())
T=list(map(int,input().split()))
C=[]
for i in range(len(T)):
    C.append((T[i],i+1))
B=[]
C.sort()
T_bar=0
for i in range(len(C)):
    B.append(C[i][1])
    T_bar+=C[i][0]*(len(C)-i-1)
print(*B)
T_bar=T_bar/len(C)
print("%.2f"%T_bar)




