class Solution:
    def is_square_of_size_win(self, matrix, r, c, win):
        for rw in range(win):
            for cw in range(win):
                if matrix[r + rw][c + cw] == 0:
                    return False
        return True
                

    def has_square_of_size_win(self, matrix, win):
        int_matrix = [[int(elem) for elem in row ]for row in matrix]
        rows, cols = len(matrix), len(matrix[0])
        
        for r in range(rows - win + 1):
            for c in range(cols - win + 1):
                if self.is_square_of_size_win(int_matrix, r, c, win):
                    return True
        return False
                        
        
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 1, min(rows, cols)
        best = 0
        while left <= right:
            mid = (left + right) // 2
            if self.has_square_of_size_win(matrix, mid):
                best = mid * mid
                left = mid + 1
            else:
                right = mid - 1    
        return best