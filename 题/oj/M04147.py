def Hanuota(a,b,c,N):
     if N==1:
         print(f"{1}:{a}->{c}")
     else:
         Hanuota(a,c,b,N-1)
         print(f"{N}:{a}->{c}")
         Hanuota(b,a,c,N-1)
n,a,b,c=input().split()
N=int(n)
Hanuota(a,b,c,N)