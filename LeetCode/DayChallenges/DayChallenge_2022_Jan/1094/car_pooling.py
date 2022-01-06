from heapq import heappush, heappop
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x:x[1])
        car = []
        curr = 0
        for num, src, dst in trips:
            while car and car[0][0] <= src:
                _, off_num = heappop(car)
                curr -= off_num
            heappush(car, (dst, num))
            curr += num
            if curr > capacity: 
                return False
        return True
        