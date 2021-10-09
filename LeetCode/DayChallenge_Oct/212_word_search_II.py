class Trie:
    def __init__(self):
        self.root = dict()
        
    def insert(self, word):
        curr = self.root
        word += '0'
        for letter in word:
            curr.setdefault(letter, dict())
            curr = curr[letter]

class Solution:
    def _DFS(self, new_pos, board, trie_loc, word, visited, result):
        x, y = new_pos
        # 종료 조건
        if '0' in trie_loc:
            if not word in result:
                result.append(word)
            if len(trie_loc) == 1:
                return
        
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            # 보드 벗어나는 경우     
            if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]):
                continue
            if (nx, ny) in visited:
                continue 
            if not board[nx][ny] in trie_loc:
                continue

            visited.add((nx, ny))
            word += board[nx][ny]
            self._DFS((nx, ny), board, trie_loc[board[nx][ny]], word, visited, result) 
            visited.remove((nx, ny))
            word = word[:-1]


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # make trie
        word_trie = Trie()
        for word in words: 
            word_trie.insert(word)
        
        root = word_trie.root
        x = 0
        y = 0

        result = []
        m = len(board)
        n = len(board[0])
        for x in range(m):
            for y in range(n):
                if board[x][y] in root:
                    visited = set()
                    visited.add((x, y))
                    self._DFS((x, y), board, root[board[x][y]], board[x][y], visited, result)
        return result