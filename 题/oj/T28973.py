from collections import deque
n=int(input())
matrix=[]
for _ in range(n):
    matrix.append(list(map(int,input().split())))

def bfs(i_h,j_h,i):
    q=deque([(0,(i_h,j_h,i))])#i=0是水平
    in_queue={(i_h,j_h,i)}
    while q:
        step,(r_h,c_h,j)=q.popleft()
        if r_h==n-1 and c_h==n-1 and j==0:
            return step
        #1:(r_h,c_h,1)->(r_h+1,c_h,1);2:(r_h,c_h,0)->(r_h,c_h+1,0)
        #3:(r_h,c_h,0)->(r_h+1,c_h-1,1);4:(r_h,c_h,1)->(r_h-1,c_h+1,0)
        if j==1 and 0<=r_h+1<n and 0<=c_h<n and matrix[r_h+1][c_h]!=1 and (r_h+1,c_h,j) not in in_queue:
            q.append((step+1,(r_h+1,c_h,j)))
            in_queue.add((r_h+1,c_h,j))
        if j==1 and 0<=r_h<n and 0<=c_h+1<n and matrix[r_h][c_h+1]!=1 and matrix[r_h-1][c_h+1]!=1 and (r_h,c_h+1,j) not in in_queue:
            q.append((step+1,(r_h,c_h+1,j)))
            in_queue.add((r_h,c_h+1,j))
        if j==0 and 0<=r_h<n and 0<=c_h+1<n and matrix[r_h][c_h+1]!=1 and (r_h,c_h+1,j) not in in_queue:
            q.append((step+1,(r_h,c_h+1,j)))
            in_queue.add((r_h,c_h+1,j))
        if j==0 and 0<=r_h+1<n and 0<=c_h<n and matrix[r_h+1][c_h]!=1 and matrix[r_h+1][c_h-1]!=1 and (r_h+1,c_h,j) not in in_queue:
            q.append((step+1,(r_h+1,c_h,j)))
            in_queue.add((r_h+1,c_h,j))
        if j==0 and 0<=r_h+1<n and 0<=c_h-1<n and matrix[r_h+1][c_h-1]!=1 and matrix[r_h+1][c_h]!=1 and (r_h+1,c_h-1,j-1) not in in_queue:
            q.append((step+1,(r_h+1,c_h-1,j+1)))
            in_queue.add((r_h+1,c_h-1,j+1))
        if j==1 and 0<=r_h-1<n and 0<=c_h+1<n and matrix[r_h-1][c_h+1]!=1 and matrix[r_h][c_h+1]!=1 and (r_h-1,c_h+1,j-1) not in in_queue:
            q.append((step+1,(r_h-1,c_h+1,j-1)))
            in_queue.add((r_h-1,c_h+1,j-1))
    return -1
print(bfs(0,1,0))