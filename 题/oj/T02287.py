while True:
    try:
        n=int(input())
        Tianji_speed=sorted(map(int,input().split()),reverse=True)
        King_speed=sorted(map(int,input().split()),reverse=True)
        fast_tian,fast_king=0,0
        slow_tian,slow_king=n-1,n-1
        win=0
        for i in range(n):
            if Tianji_speed[fast_tian]>King_speed[fast_king]:
                win+=200
                fast_tian+=1
                fast_king+=1
            elif Tianji_speed[slow_tian]>King_speed[slow_king]:
                win+=200
                slow_tian-=1
                slow_king-=1
            else:
                if Tianji_speed[slow_tian]<King_speed[fast_king]:
                    win-=200
                slow_tian-=1
                fast_king+=1
        print(win)
    except EOFError:
        break