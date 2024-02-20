class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda a:a[1])  
        x, count = points[0][1], 1
        for i in range(1,len(points)):
            if not points[i][0] <= x <= points[i][1]:
                x = points[i][1]
                count += 1
        return count