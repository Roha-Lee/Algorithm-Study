class Solution:
    def tribonacci(self, n: int) -> int:
        DP = [0] * (n+3)
        DP[1] = DP[2] = 1
        for i in range(3, n+1):
            DP[i] = DP[i-3] + DP[i-2] + DP[i-1]
        return DP[n]
        