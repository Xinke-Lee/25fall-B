N=int(input())
dicta=[]
for a in range(1,N+1):
    for b in range(2,a):
        for c in range(b,a):
            for d in range (c,a):
                if a**3==b**3+c**3+d**3:
                    dicta.append((a,b,c,d))
sorted_dict=sorted(dicta)
for (a,b,c,d) in sorted_dict:
    print(f"Cube = {a}, Triple = ({b},{c},{d})")