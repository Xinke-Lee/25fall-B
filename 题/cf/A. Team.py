N=input().strip()
n=int(N)
number=0
for i in range(n):
    result=list(map(int,input().split()))
    result.sort()
    if result[0]==0 and result[1]==0 and result[2]==0:
        number+=0
    elif result[0]==0 and result[1]==0 and result[2]==1:
        number+=0
    else:
        number+=1
print(number)

