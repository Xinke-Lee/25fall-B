import math
while True:
        N=int(input())
        if N==0:
           break
        Tf=[]
        for i in range(N):
            Vi,Ti=map(int,input().split())
            if Ti>=0:
                Tf.append(math.ceil(Ti+4.5*3600/Vi))
        print(min(Tf))    
        