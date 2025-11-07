n=int(input())
num=list(map(int,input().split()))
n1=num.count(1)
n2=num.count(2)
n3=num.count(3)
n4=num.count(4)
if n3>n1:
   if n2%2==0:
      N=n4+n2//2+n3
   else:
      N=n4+n2//2+n3+1
else:
   if n2%2==0:
      if (n1-n3)%4==0:
         N=n4+n2//2+n3+(n1-n3)//4
      else:
         N=n4+n2//2+n3+(n1-n3)//4+1
   else:
      if (n1-n3)>2:
         if (n1-n3-2)%4==0:
            N=n4+n2//2+n3+(n1-n3-2)//4+1
         else:
            N=n4+n2//2+n3+(n1-n3-2)//4+2
      else:
         N=n4+n2//2+n3+1
print(N)