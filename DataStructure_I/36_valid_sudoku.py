class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_count = [[0] * 9 for _ in range(9)] 
        row_count = [[0] * 9 for _ in range(9)] 
        block_count = [[0] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elem = int(board[i][j]) - 1
                block_i = int(i//3) * 3 + int(j//3)
                if col_count[j][elem] or row_count[i][elem] or block_count[block_i][elem]:
                    return False
                col_count[j][elem] += 1
                row_count[i][elem] += 1
                block_count[block_i][elem] += 1 
        return True

