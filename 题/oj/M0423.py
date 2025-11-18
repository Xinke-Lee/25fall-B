T=int(input())
for _ in range(T):
    n,m,x,y=map(int,input().split())
    check=[[False]*m for _ in range(n)]
    check[x][y]=True
    def horse_move_like_sun(times,x,y):
        nums=0
        if times==m*n-1:
            return 1
        else:
            move=[(x+1,y+2),(x+2,y+1),(x-1,y+2),(x-2,y+1),(x-2,y-1),(x-1,y-2),(x+1,y-2),(x+2,y-1)]
            for i in move:
                if 0<=i[0]<n and 0<=i[1]<m:
                    if not check[i[0]][i[1]]:
                        check[i[0]][i[1]]=True
                        nums+=horse_move_like_sun(times+1,i[0],i[1])
                        check[i[0]][i[1]]=False
        return nums
    print(horse_move_like_sun(0,x,y))
