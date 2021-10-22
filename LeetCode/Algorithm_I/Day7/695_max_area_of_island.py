class Solution:
    def count_area(self, grid, sr, sc, cnt=0):
        if grid[sr][sc] == 0:
            return cnt 
        grid[sr][sc] = 0
        cnt += 1
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row = len(grid)
        col = len(grid[0])
        
        for dr, dc in moves:
            nr, nc = sr + dr, sc + dc
            if -1 < nr and nr < row and -1 < nc and nc < col:
                cnt = self.count_area(grid, nr, nc, cnt)
        return cnt
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        max_area = 0
        for r in range(row):
            for c in range(col):
                area = self.count_area(grid, r, c)
                if area > max_area:
                    max_area = area
        return max_area