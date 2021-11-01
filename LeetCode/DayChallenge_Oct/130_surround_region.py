class Solution:
    def dfs(self, board, r, c, visited):
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(board)
        cols = len(board[0])
        visited[r][c] = True
        board[r][c] = 'E'
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and board[nr][nc] == 'O':
                self.dfs(board, nr, nc, visited)
            
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board is None: return 
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r == 0 or c == 0 or r == len(board)-1 or c == len(board[0])-1) and board[r][c] == 'O' and not visited[r][c]:
                    self.dfs(board, r, c, visited)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'E':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
                             
        
        