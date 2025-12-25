class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        preR=-10e9
        num=0
        for point in points:
            if point[0]<=preR:
                preR=point[1]
                num+=1
        return len(points)-num