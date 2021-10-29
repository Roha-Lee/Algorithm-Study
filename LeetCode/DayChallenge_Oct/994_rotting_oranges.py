class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False] * col for _ in range(row)]
        stack = []
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    stack.append((r, c))
                    visited[r][c] = True
                    
        time = -1
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while stack:
            current_stack = []        
            while stack:
                current_stack.append(stack.pop())
                
            time += 1
            while current_stack:
                r, c = current_stack.pop()
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc] and grid[nr][nc] == 1:
                        visited[nr][nc] = True
                        grid[nr][nc] = 2
                        stack.append((nr, nc))
        
        possible = True
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    possible = False
        if possible: 
            return max(time, 0)
        else:
            return -1
                    
        
                    
            
        