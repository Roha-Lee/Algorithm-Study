from collections import deque
class Solution:        
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        visited = [[False] * col for _ in range(len(mat))]
        q = deque()
        for r in range(row):
            for c in range(col):                
                if mat[r][c] == 0:
                    q.append((r, c))
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.popleft()
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    if mat[nr][nc] != 0:
                        mat[nr][nc] = mat[r][c] + 1
            
        return mat