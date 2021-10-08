class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pos_x, pos_y = len(matrix)-1, 0
        while True:
            if target < matrix[pos_x][pos_y]:
                pos_x -= 1
            elif target > matrix[pos_x][pos_y]:
                pos_y += 1
            else:
                return True
            if not(0 <= pos_x and pos_x < len(matrix)):
                return False 
            if not(0 <= pos_y and pos_y < len(matrix[0])):
                return False 

