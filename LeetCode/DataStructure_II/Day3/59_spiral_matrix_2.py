class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        x = y = 0
        
        #(dx, dy)
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dx = 1
        dy = 0
        
        for num in range(1, n*n+1):
            matrix[y][x] = num
            if not(y + dy < n and \
                y + dy >= 0 and \
                x + dx < n and \
                x + dx >= 0 and \
                matrix[y+dy][x+dx] == 0):    
                new_index = (moves.index((dx, dy)) + 1) % 4
                dx, dy = moves[new_index]    
            y = y + dy
            x = x + dx
                
        return matrix