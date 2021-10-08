col, row = list(input().strip())
COLS = list('0abcdefgh')
col = COLS.index(col)
row = int(row)

moves = [
  (-1, -2), 
  (1, -2), 
  (2, -1), 
  (2, 1), 
  (1, 2), 
  (-1, 2), 
  (-2, 1), 
  (-2, -1)
]

result = 0
for dx, dy in moves:
    if row + dy < 9 and 0 < row + dy and col + dx < 9 and 0 < col + dx:
        result += 1
print(result)


