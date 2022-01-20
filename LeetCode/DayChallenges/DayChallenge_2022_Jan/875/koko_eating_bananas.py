from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        beg, end = 0, max(piles)
        while beg + 1 < end:
            mid = (beg + end)//2
            if sum(ceil(i/mid) for i in piles) > h:
                beg = mid
            else:
                end = mid
                
        return end