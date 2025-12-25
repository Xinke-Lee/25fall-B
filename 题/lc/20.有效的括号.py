class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        left=['{','[','(']
        right=['}',']',')']
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if not stack:
                    return False
                if left.index(stack.pop())!=right.index(c):
                    return False
        return not stack