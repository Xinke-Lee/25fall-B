class Solution:
    def simplifyPath(self, path: str) -> str:
        document=list(path.split('/'))
        stack=[]
        for s in document:
            if s=='.':
                continue
            elif s=='':
                continue
            elif s=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        return '/'+'/'.join(stack)