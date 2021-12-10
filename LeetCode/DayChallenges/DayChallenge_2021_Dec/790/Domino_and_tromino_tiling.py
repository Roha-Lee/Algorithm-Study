class Solution:
    def numTilings(self, n: int) -> int:
        DP = [0] * max(3, n+1)
        DP[0] = 1
        DP[1] = 1
        DP[2] = 2
        for i in range(3, n+1):
            DP[i] = DP[i-1] + DP[i-2]
            for j in range(i-2):
                DP[i] += 2 * DP[j]
        return DP[n] % (10**9 + 7)