n=int(input())
num_ijn=[]
for i in range(n):
    s=int(input())
    a=int(input())
    A=list(map(int,input().split()))
    b=int(input())
    B=list(map(int,input().split()))
    num_ij=0
    for pi in A:
        for qj in B:
            if pi+qj==s:
                num_ij+=1
    num_ijn.append(num_ij)
for i in range(n):
    print(num_ijn[i])
    #时间复杂度太高了！下面是优化
''' 
n = int(input().strip())
results = []
for _ in range(n):
    s = int(input().strip())
    a = int(input().strip())
    A = list(map(int, input().split()))
    b = int(input().strip())
    B = list(map(int, input().split()))
    
    freq_B = {}
    for num in B:
        freq_B[num] = freq_B.get(num, 0) + 1
        
    count = 0
    for p in A:
        need = s - p
        if need in freq_B:
            count += freq_B[need]
            
    results.append(count)

for res in results:
    print(res)
    '''
