def check(j, i, map):
    for m in range(j):
        if map[m] == i or abs(map[m] - i) == abs(m - j):
            return False
    return True
n=8
Ans = []
map=[-1]*n
def queen(j, n, map):
    if j == n:
        Ans.append(map[:])
        return
    for i in range(n):
        if check(j, i, map):
            map[j] = i
            queen(j + 1, n, map)
            map[j] = -1
n=int(input())
queen(0,8,map)

Ans1=[]
for i in Ans:
    a=0
    for j in range(8):
        a+=(i[j]+1)*(10**(8-j-1))
    Ans1.append(a)
Ans1.sort()

for _ in range(n):
    i=int(input())
    print(Ans1[i-1])
