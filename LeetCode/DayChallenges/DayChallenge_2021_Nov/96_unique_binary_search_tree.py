class Solution:
    def numTrees(self, n: int) -> int:
        DP = [0] * (n+1)
        DP[0] = 1
        DP[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                DP[i] += DP[j] * DP[i-1-j]    
        return DP[n]