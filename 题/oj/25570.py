n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
a=(n+1)//2
sum1=[]
j=0
while a>0:
    sum=0
    for m in range(j,n-j):
        sum+=matrix[m][j]+matrix[j][m]+matrix[n-1-j][m]+matrix[m][n-1-j]
    sum-=matrix[j][j]+matrix[n-1-j][j]+matrix[j][n-1-j]+matrix[n-1-j][n-1-j]
    j+=1
    a-=1
    sum1.append(sum)
if n%2!=0:
    sum1.pop()
    sum1.append(matrix[(n+1)//2-1][(n+1)//2-1])
print(max(sum1))