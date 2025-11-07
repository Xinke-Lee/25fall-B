n, m1, m2 = map(int, input().split())
M1 = {}
M2 = {}
M3 = {}
for _ in range(m1):
    i, j, aij = map(int, input().split())
    if i not in M1:
        M1[i] = {}
    M1[i][j] = aij
for _ in range(m2):
    i, j, bij = map(int, input().split())
    if i not in M2:
        M2[i] = {}
    M2[i][j] = bij
for (i, l_line) in M1.items():
    for (l, ail) in l_line.items():
        if l in M2:
            for (j, blj) in M2[l].items():
                key = (i, j)
                cij = M3.get(key, 0)
                M3[key] = cij + ail * blj
output = []
for (i, j), v in M3.items():
    if v != 0:
        output.append((i, j, v))
output.sort()
for item in output:
    print(*item)