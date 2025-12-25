t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    nums=list(map(int,input().split()))
    if n==1:
        if nums[0]%x!=0:
            print(1)
        else:
            print(-1)
    else:
        total=sum(nums)
        left=-1
        right=-1
        if total%x!=0:
            print(len(nums))
        else:
            for i in range(len(nums)):
                if nums[i]%x!=0:
                    left=i
                    break
            nums.reverse()
            for i in range(len(nums)):
                if nums[i]%x!=0:
                    right=i
                    break
            if left==right==-1:
                print(-1)
            else:
                print(len(nums)-min(left,right)-1)