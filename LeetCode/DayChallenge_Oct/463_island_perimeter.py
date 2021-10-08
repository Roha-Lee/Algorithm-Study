class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        rows = len(grid)
        cols = len(grid[0])
        total_perimeter = 0
        for r in range(rows):
            for c in range(cols):
                if not grid[r][c]:
                    continue
                perimeter = 4
                for dr, dc in moves:
                    _r = r + dr if r + dr >= 0 and r + dr < rows else -1
                    if _r == -1:
                        continue
                    _c = c + dc if c + dc >= 0 and c + dc < cols else -1
                    if _c == -1:
                        continue
                    perimeter -= grid[_r][_c]
                total_perimeter += perimeter
        return total_perimeter
                    
                    
        