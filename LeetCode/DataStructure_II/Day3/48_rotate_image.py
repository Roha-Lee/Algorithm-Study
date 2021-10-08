class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        repeat = int(col // 2)
        for depth in range(repeat):
            for x in range(depth, row - depth - 1):
                matrix[depth][x], matrix[x][row-1-depth], matrix[row-1-depth][col-1-x], matrix[col-1-x][depth] = matrix[col-1-x][depth], matrix[depth][x], matrix[x][row-1-depth], matrix[row-1-depth][col-1-x]
        return matrix
                