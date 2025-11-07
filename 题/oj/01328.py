import math
Case = 0
while True:
    line = input()
    if not line: continue
    n, d = map(int, line.split())
    if (n, d) == (0, 0):
        break
    Case += 1
    intervals = []
    possible = True
    for _ in range(n):
        x, y = map(int, input().split())
        if y > d or d < 0:
            possible = False
        if possible:
            offset = math.sqrt(d ** 2 - y ** 2)
            intervals.append((x - offset, x + offset))

    try:
        input()
    except (EOFError, ValueError):
        pass

    if not possible:
        print(f"Case {Case}: -1")
        continue

    intervals.sort(key=lambda item: item[1])
    count = 0
    last_pos = -float('inf')
    for left, right in intervals:
        if left > last_pos:
            count += 1
            last_pos = right
    print(f"Case {Case}: {count}")



