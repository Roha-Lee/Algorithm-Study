class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        DP = [[1] * n for _ in range(m)]
        for r in range(1, m):
            for c in range(1, n):
                DP[r][c] = DP[r-1][c] + DP[r][c-1]
        return DP[-1][-1]
        