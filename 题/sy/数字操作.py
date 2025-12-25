from collections import deque
def bfs(start, end):
    q = deque([(0, start)])  # (step, start)
    in_queue = {start}
    while q:
        step, front = q.popleft()  # 取出队首元素
        if front == end:
            return step
        a=front+1
        b=2*front
        if a not in in_queue and a<=n:
            in_queue.add(a)
            q.append((step+1,a))
        if b not in in_queue and b<=n:
            in_queue.add(b)
            q.append((step+1,b))
n=int(input())
print(bfs(1,n))



