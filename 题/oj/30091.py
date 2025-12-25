L = int(input().strip())
N = int(input().strip())
if N == 0:
    print("0 0")
else:
    positions = list(map(int, input().split()))
    min_time = 0
    max_time = 0
    for p in positions:
        left_time = p
        right_time = L + 1 - p
        min_time = max(min_time, min(left_time, right_time))
        max_time = max(max_time, max(left_time, right_time))
    print(min_time, max_time)