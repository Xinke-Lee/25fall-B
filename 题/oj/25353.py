import sys
N,D = map(int,input().split())
H=[int(sys.stdin.readline()) for _ in range(N)]
while len(H)>1:
    H_available = []
    H_unavailable = []
    h_max=-1
    h_min=float('inf')
    for i in H:
        if i==0:
            H_available.append(i)
        else:
            if i-h_min<=D and -i+h_max<=D:
                H_available.append(i)
            else:
                H_unavailable.append(i)
        h_max=max(h_max,i)
        h_min=min(h_min,i)
    H=list(H_unavailable[:])
    for jj in sorted(H_available):
        print(jj)
