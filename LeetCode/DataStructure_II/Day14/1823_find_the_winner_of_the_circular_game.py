class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        candidates = list(range(1, n+1))
        start = 0
        while n > 1:
            start = (start + k - 1) % n
            candidates.pop(start)
            n = len(candidates)
            
        return candidates[0]