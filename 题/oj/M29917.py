import sys
for line in sys.stdin:
    n = float(line.strip())
    A = 0
    x = 1
    while True:
        if abs((x ** 2 - n) / (2 * x)) <= 0.000001:
            break
        else:
            x = x - (x ** 2 - n) / (2 * x)
            A += 1
    print(f"{A+1} {x:.2f}")