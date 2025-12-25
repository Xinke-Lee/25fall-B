import sys
input = sys.stdin.read
data_input = input().split()
iterator = iter(data_input)
try:
    n = int(next(iterator))
    m = int(next(iterator))
except StopIteration:
    exit()
sums = []
x = []
raw_data = []
for _ in range(n):
    xi = int(next(iterator))
    yi = int(next(iterator))
    sums.append(xi + yi)
    x.append(xi)
    raw_data.append((xi, yi))
a=min(sums)
idx=sums.index(a)
x0=raw_data[idx][0]
y0=raw_data[idx][1]
x_others=[]
for i in range(n):
    if i!=idx:
        x_others.append(x[i])
x = x_others
x.sort()
all_x = sorted([p[0] for p in raw_data])
temp_sum = 0
k = 0
for cost in all_x:
    if temp_sum + cost <= m:
        temp_sum += cost
        k += 1
    else:
        break
sum_i = 0
if m >= x0:
    rest=m-x0
    times=1+(rest//a)*2
    if rest%a>=y0:
        times+=1
    if times>k:
        k=times
for i in range(len(x)):
    sum_i+=x[i]
    total_cost=x0+sum_i
    if total_cost>m:
        break
    rest=m-total_cost
    times=(i+2)+(rest//a)*2
    if rest%a>=y0:
        times+=1
    if times>k:
        k=times
print(k)