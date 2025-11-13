def count1(a):
    sum_val = 0
    while a > 0:
        sum_val += a % 10
        a = a // 10
    return sum_val

m, n, k = map(int, input().split(','))
groups = {}

for i in range(m + 1, n):
    digit_sum = count1(i)
    if digit_sum % k == 0:
        if digit_sum not in groups:
            groups[digit_sum] = []
        groups[digit_sum].append(i)

for digit_sum in sorted(groups.keys()):
    result = ','.join(map(str, groups[digit_sum]))
    print(result)