class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        dp=[0]*(n+1)
        dp[-1]=questions[-1][0]
        for i in range(n-1,0,-1):
            points=questions[i][0]
            brainpower=questions[i][1]
            if i+brainpower+1>n:
                add=points
            else:
                add=points+dp[i+brainpower+1]
            dp[i]=max(add,dp[i+1])
        return max(dp)