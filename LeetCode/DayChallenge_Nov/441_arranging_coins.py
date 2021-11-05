class Solution:
    def arrangeCoins(self, n: int) -> int:
        s, e = 0, n 
        best = 0
        while s <= e: 
            mid = (s + e) // 2
            val = mid * (mid + 1) //2
            if val <= n:
                s = mid + 1
                best = mid
            else:
                e = mid - 1
            
        return best