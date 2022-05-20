class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1: return 0
        num_row = len(obstacleGrid)
        num_col = len(obstacleGrid[0])
        DP = [[0] * num_col for _ in range(num_row)]
        DP[0][0] = 1
        for r in range(num_row):
            for c in range(num_col):
                if r == 0 and c == 0: continue
                if obstacleGrid[r][c] == 1: continue
                if r == 0:
                    DP[r][c] = DP[r][c-1]
                elif c == 0:
                    DP[r][c] = DP[r-1][c]
                else:
                    DP[r][c] = (DP[r-1][c] or 0) + (DP[r][c-1] or 0)
        return DP[-1][-1]