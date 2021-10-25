import sys 
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)
test_num = int(input())
# bfs time limit exceed!
def bfs(grid, sr, sc, n, m): 
    q = deque()
    q.append((sr, sc))
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        sr, sc = q.popleft()
        grid[sr][sc] = 0
        for dr, dc in moves:
            nr, nc = sr + dr, sc + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc]:
                q.append((nr, nc))

def dfs(grid, sr, sc, n, m):
    grid[sr][sc] = 0
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dr, dc in moves:
        nr, nc = sr + dr, sc + dc
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc]:
            dfs(grid, nr, nc, n, m)
for _ in range(test_num):
    m, n, k = map(int, input().split())
    grid = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        grid[y][x] = 1
    
    cnt = 0 
    for r in range(n):
        for c in range(m):
            if grid[r][c]:
                cnt += 1
                bfs(grid, r, c, n, m)
    print(cnt)
