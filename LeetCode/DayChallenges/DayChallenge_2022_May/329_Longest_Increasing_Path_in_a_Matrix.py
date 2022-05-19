class Solution:
    def __init__(self):
        self.num_row = 0
        self.num_col = 0
        self.matrix = None
        self.visited = None
        self.path_length = None
        self.answer = 1
        
    def dfs(self, r, c):
        self.visited[r][c] = True
        moves = [(1, 0), (0 , 1), (-1, 0), (0, -1)]
        for dr, dc in moves:
            nr, nc = r + dr, c + dc 
            if not (0 <= nr < self.num_row and 0 <= nc < self.num_col):
                continue
            if self.matrix[r][c] < self.matrix[nr][nc]:
                if self.visited[nr][nc]:
                    self.path_length[r][c] = max(self.path_length[r][c], self.path_length[nr][nc] + 1)
                else:
                    self.path_length[r][c] = max(self.path_length[r][c], self.dfs(nr, nc) + 1)            
        self.answer = max(self.path_length[r][c], self.answer)
        return self.path_length[r][c]
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.num_row = len(matrix)
        self.num_col = len(matrix[0])
        self.visited = [[False] * self.num_col for _ in range(self.num_row)]
        self.path_length = [[1] * self.num_col for _ in range(self.num_row)]
        self.matrix = matrix
        for r in range(self.num_row):
            for c in range(self.num_col):
                if not self.visited[r][c]:
                    self.dfs(r, c)
        return self.answer