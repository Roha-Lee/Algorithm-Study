class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        DP = [[0] * cols for _ in range(rows)]
        result = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '0':
                    DP[r][c] = 0
                    continue
                if r == 0 or c == 0:
                    DP[r][c] = 1 
                else:
                    DP[r][c] = min(DP[r-1][c], DP[r][c-1], DP[r-1][c-1]) + 1
                result = max(result, DP[r][c] **2)  
        return result