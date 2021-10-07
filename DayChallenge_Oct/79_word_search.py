
class Solution:
    def DFS(self, board, word, cur_pos, candidate):
        if len(candidate) == len(word):
            if not board[cur_pos[0]][cur_pos[1]] == word[-1]:
                return False
            return True
            
        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m = len(board)
        n = len(board[0])
        cur_index = len(candidate)
        for dx, dy in moves:
            trial_x, trial_y = cur_pos
            trial_x, trial_y = trial_x + dx, trial_y + dy
            if trial_x < 0 or trial_x >= m or trial_y < 0 or trial_y >= n:
                continue
            
            if (trial_x, trial_y) in candidate:
                continue
                
            if not word[cur_index] == board[trial_x][trial_y]:
                continue
            candidate.add((trial_x, trial_y))
            if self.DFS(board, word, (trial_x, trial_y), candidate):
                return True
            else:
                candidate.remove((trial_x, trial_y))
            
            
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                candidate = set()
                if not word[0] == board[i][j]:
                    continue
                candidate.add((i, j))
                if self.DFS(board, word, (i, j), candidate):
                    return True
        return False
        
# Time Limit Exceed!
# class Solution:
#     def is_available(self, board, visited, word, cur_pos, candidate):
#         # 판을 벗어났는지 체크 
#         x, y = cur_pos
#         if x < 0 or x >= len(visited):
#             return False
#         if y < 0 or y >= len(visited[0]):
#             return False
        
#         # visited를 다시 방문했는지 체크 
#         if visited[x][y]:
#             return False
        
#         # 글자 같은지 체크 
#         cur_index = len(candidate)
#         if not word[cur_index] == board[x][y]:
#             return False
        
#         return True
            
#     def DFS(self, results, board, visited, word, cur_pos, candidate):
#         if len(word) == 1 and board[cur_pos[0]][cur_pos[1]] == word:
#             results.append([cur_pos])
#             return 
        
#         if len(candidate) == len(word):
#             results.append(candidate[:])
#             return 
        
#         moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
#         for dx, dy in moves:
#             trial_x, trial_y = cur_pos
#             trial_x, trial_y = trial_x + dx, trial_y + dy
#             if self.is_available(board, visited, word, (trial_x, trial_y), candidate):
#                 candidate.append((trial_x, trial_y))
#                 visited[trial_x][trial_y] = True
#                 self.DFS(results, board, visited, word, (trial_x, trial_y), candidate)
#                 candidate.pop()
#                 visited[trial_x][trial_y] = False
                
            
        
            
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 results = []
#                 visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
#                 self.DFS(results, board, visited, word, (i, j), [])
#                 if len(results) > 0:
#                     return True
#         return False