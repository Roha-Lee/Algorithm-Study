import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        priority_queue = []
        prev = heights[0]
        for index, height in enumerate(heights):
            diff = height - prev
            prev = height
            if diff <= 0: continue
            heapq.heappush(priority_queue, diff)
            if ladders: 
                ladders -= 1
            else:
                bricks -= heapq.heappop(priority_queue)
            if bricks < 0: return index - 1
        return len(heights) - 1