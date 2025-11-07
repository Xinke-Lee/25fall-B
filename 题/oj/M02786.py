def pell(k):
    if k == 1:
        return 1
    elif k == 2:
        return 2

    a1, a2 = 1, 2
    for i in range(3, k + 1):
        a1, a2 = a2, (2 * a2 + a1) % 32767

    return a2

n = int(input())
for _ in range(n):
    k = int(input())
    print(pell(k))


