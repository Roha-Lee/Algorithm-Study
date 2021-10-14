# DP로 풀어
class Solution:
    def numSquares(self, n: int) -> int:
        DP = [0] * (n+1)
        squares = [x*x for x in range(2, 101)]
        for i in range(1, n+1):
            DP[i] = DP[i-1] + 1
            for square in squares:
                if i - square >= 0:
                    DP[i] = min(DP[i-square] + 1, DP[i])
                else:
                    break
            
        return DP[-1]