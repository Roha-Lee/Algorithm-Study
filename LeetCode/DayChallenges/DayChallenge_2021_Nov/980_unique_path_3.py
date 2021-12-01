class Solution:    
    def dfs(self, grid, r, c, max_val, result, results):
        rows = len(grid)
        cols = len(grid[0])
        if len(result) == max_val:
            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2:
                    results.append(result[:])
            return
        
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                grid[nr][nc] = 3
                result.append((nr, nc))
                self.dfs(grid, nr, nc, max_val, result, results)
                result.pop()
                grid[nr][nc] = 0  
                
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_val = 0
        sr, sc = 0, 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    sr, sc = r, c
                elif grid[r][c] == 0:
                    max_val += 1
        results = []
        self.dfs(grid, sr, sc, max_val, [], results)
        return len(results)