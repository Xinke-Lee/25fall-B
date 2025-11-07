N,M,A=input().split()
n,m,a=int(N),int(M),int(A)
p=0
q=0
if n%a==0:
   p=n//a
else:
   p=n//a+1
if m%a==0:
   q=m//a
else:
   q=m//a+1  
print(p*q) 
