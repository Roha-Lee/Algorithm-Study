import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = list(map(lambda p: (p[0]*p[0] + p[1]*p[1], p[0], p[1]), points))
        heapq.heapify(q)
        result = []
        for i in range(k):
            _, x, y = heapq.heappop(q)
            result.append([x, y])
        return result            
        