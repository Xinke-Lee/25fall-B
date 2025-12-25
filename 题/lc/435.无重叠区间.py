class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        num=0
        preR=-10e9
        for i in intervals:
            if i[0]>=preR:
                preR=i[1]
                num+=1
        return len(intervals)-num
