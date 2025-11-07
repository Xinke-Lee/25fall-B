inputs=[]
outputs=[]
while True:
    m=input().strip()
    n=float(m)
    if m=='0.00':
        break
    inputs.append(n)
for i in inputs:
        a=0
        c=2
        while True:
            a+=1/c
            c+=1
            if i-a>0 and i-a-1/(c+1)<0:
                outputs.append(str(c)+' card(s)')
                break 
for o in outputs:
    print(o)
    #这个结果超时了！
