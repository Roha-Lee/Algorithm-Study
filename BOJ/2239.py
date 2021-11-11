import sys 
def generate_sudoku(sudoku, num=0):
    # print(num)
    if num == 81:
        for i in range(9):
            print(''.join(list(map(str, sudoku[i]))))
        return True
    
    r = num // 9
    c = num % 9 
    b = (r // 3) * 3 + (c // 3)

    if sudoku[r][c] == 0:
        # need to solve
        for i in range(1, 10):
            if horizontal[r][i-1] or vertical[c][i-1] or block[b][i-1]:
                continue
            horizontal[r][i-1] = vertical[c][i-1] = block[b][i-1] = True
            sudoku[r][c] = i
            if generate_sudoku(sudoku, num + 1):
                return True
            sudoku[r][c] = 0
            horizontal[r][i-1] = vertical[c][i-1] = block[b][i-1] = False
        
    else:
        return generate_sudoku(sudoku, num + 1)
    return False

if __name__ == '__main__':
    input = sys.stdin.readline
    block = [[False] * 9 for _ in range(9)]
    horizontal = [[False] * 9 for _ in range(9)]
    vertical = [[False] * 9 for _ in range(9)]
    
    sudoku = []
    for i in range(9):
        sudoku.append(list(map(int, input().rstrip())))
    
    for r in range(9):
        for c in range(9):
            if sudoku[r][c]:
                number = sudoku[r][c] - 1
                horizontal[r][number] = True
                vertical[c][number] = True
                block[(r // 3) * 3 + (c // 3)][number] = True
    generate_sudoku(sudoku)