class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        DP = [0] * (n+1)
        DP[1] = 1
        for i in range(2, n+1):
            DP[i] = DP[i-1] + DP[i-2]
        return DP[n]
            