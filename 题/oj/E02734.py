a=int(input())
b=0
c=[]
while True:
    b=a//8
    c.append(a%8)
    a=b
    if b==0:
        break
c.reverse()
print(''.join(map(str,c[0:len(c)])))