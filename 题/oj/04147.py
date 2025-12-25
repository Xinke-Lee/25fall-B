n,a,b,c=input().split()
N=int(n)

def Hanoi(Na,ha,hb,hc):
    if Na==0:
        return
    else:
        Hanoi(Na-1,ha,hc,hb)
        print(f"{Na}:{ha}->{hc}")
        Hanoi(Na-1,hb,ha,hc)

Hanoi(N,a,b,c)
