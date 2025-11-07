n=int(input().strip())
dates=[31,28,31,30,31,30,31,31,30,31,30,31]
numbers=[]
for i in range(1,n+1):
    A,B,C,D,E=input().split()
    a=int(A)-1
    b=int(B)
    c=int(C)
    d=int(D)-1
    e=int(E)
    k=0
    l=0
    for j in range(a):
        k+=dates[j]
    first=k+b
    for r in range(d):
        l+=dates[r]
    second=l+e
    number=c*(2**(second-first))
    numbers.append(number)
for number in numbers:
    print(number)   

