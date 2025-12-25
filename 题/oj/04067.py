from collections import deque

while True:
    try:
        num=input()
        num_deque=deque(num)
        if len(num_deque)==1:
            print('YES')
        else:
            is_palindrome=True
            while len(num_deque)>1:
                a=num_deque.popleft()
                b=num_deque.pop()
                if a==b:
                    continue
                else:
                    is_palindrome=False
                    break
            if is_palindrome:
                print('YES')
            else:
                print('NO')
    except EOFError:
        break