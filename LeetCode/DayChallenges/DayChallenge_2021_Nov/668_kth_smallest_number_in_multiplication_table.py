class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left, right = 1, m * n
        best = -1
        while left <= right:
            mid = (left + right) // 2 
            curr_cnt = self.count(mid, m, n)
            
            if curr_cnt >= k:
                best = mid
                right = mid-1
            else:
                left = mid + 1
        
        return best
    
    def count(self, num, m, n):
        cnt = 0 
        for i in range(1, m+1):
            add = min(n, num // i)
            if add:
                cnt += add
            else:
                break
        return cnt
            
        