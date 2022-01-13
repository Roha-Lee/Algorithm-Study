class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x:x[1])
        answer = 1
        hold = points[0][1]
        for start, end in points[1:]:
            if hold < start:
                answer += 1
                hold = end
        return answer
            
            