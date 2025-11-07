m,n=input().split()
M=int(m)
N=int(n)
if N%2!=0:
   print(M*(N//2)+M//2)
if N%2==0:
   print(M*(N//2))