n=int(input())
height=list(map(int,input().split()))
stack=[]
ans=0
for i in range(n):
    while stack and height[i]>height[stack[-1]]:
        cur=stack.pop()
        if not stack:
            break
        left=stack[-1]
        right=i
        h=min(height[left],height[right])-height[cur]
        w=right-left-1
        ans+=h*w
    stack.append(i)
print(ans)

