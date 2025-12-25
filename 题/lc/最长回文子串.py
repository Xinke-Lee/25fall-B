from collections import deque
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(si):
            deque_s=deque(si)
            while len(deque_s)>1:
                a=deque_s.popleft()
                b=deque_s.pop()
                if a==b:
                    continue
                else:
                    return False
                    break
            return True
        length=0
        x=0
        y=0
        if len(s)>1:
            for i in range(len(s)-1):
                for j in range(i,len(s)):
                    if is_palindrome(s[i:j]):
                        if j-i+1>length:
                            length=j-i+1
                            x=i
                            y=j
            return s[x:y]
        elif len(s)==1:
            return s
#O（N3），遗憾，还是得中心扩散