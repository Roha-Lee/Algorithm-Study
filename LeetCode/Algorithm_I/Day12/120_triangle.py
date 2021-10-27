class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        result = [[float('inf') for _ in range(len(triangle[i]))] for i in range(len(triangle))]
        result[0][0] = triangle[0][0]
        for row in range(1, len(triangle)):
            for i in range(len(triangle[row])):
                if 0 <= i-1:
                    result[row][i] = min(result[row-1][i-1] + triangle[row][i], result[row][i]) 
                if i < row:
                    result[row][i] = min(result[row-1][i] + triangle[row][i], result[row][i]) 
        return min(result[-1])