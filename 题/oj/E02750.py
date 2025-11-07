a=int(input())
if a%2!=0:
    print('0 0')
if a%2==0 and a%4!=0:
    print(str(a//4+1)+' '+str(a//2))
if a%4==0:
    print(str(a//4)+' '+str(a//2))