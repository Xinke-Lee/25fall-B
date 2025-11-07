n=int(input())
for i in range(n):
    s=input()
    num=[]
    for i in range(len(s)-1):
        num.append(int(s[i]))
    sec=7*num[0]+9*num[1]+10*num[2]+5*num[3]+8*num[4]+4*num[5]+2*num[6]+1*num[7]+6*num[8]+3*num[9]+7*num[10]+9*num[11]+10*num[12]+5*num[13]+8*num[14]+4*num[15]+2*num[16]
    sec1=sec%11
    right=[(0,'1'),(1,'0'),(2,'X'),(3,'9'),(4,'8'),(5,'7'),(6,'6'),(7,'5'),(8,'4'),(9,'3'),(10,'2')]
    if (sec1,s[17]) in right:
        print('YES')
    else:
        print('NO')