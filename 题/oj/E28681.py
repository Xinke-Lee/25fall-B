n=int(input())
scores={}
for i in range(1,n+1):
    a,b,c=map(int,input().split())
    sum_score=a+b+c
    if sum_score not in scores:
        scores[sum_score]=[(a,i)]
    else:
        scores[sum_score].append((a,i))
sorted_scores = sorted(scores.keys(),reverse=True)
for score in sorted_scores:
    scores[score].sort(key=lambda x:x[0],reverse=True)
num=0
for i in sorted_scores:
    for j in scores[i]:
        if num<5:
            num+=1
            print(j[1],i)

