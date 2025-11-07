def three_tower(n):
    if n==1:
        return 1
    if n==0:
        return 0
    else:
        times=0
        times+=three_tower(n-1)
        times+=1
        times+=three_tower(n-1)
        return times

def four_tower(n):
    if n==1:
        return 1
    if n==0:
        return 0
    min_times = 0
    for i in range(1,n+1):
        times=0
        times+=four_tower(n-i)
        times+=three_tower(i)
        times+=four_tower(n-i)
        if times<min_times or min_times==0:
            min_times=times
    return min_times

for i in range(1,13):
    print(four_tower(i))





