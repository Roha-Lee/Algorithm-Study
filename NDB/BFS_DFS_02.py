from collections import deque

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input())))

def maze(i, j):
    queue = deque([(i-1, j-1)])
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        ci, cj = queue.popleft()
        for di, dj in moves:
            ni, nj = ci + di, cj + dj
            if ni < N and -1 < ni and nj < M and -1 < nj and matrix[ni][nj] == 1:
                matrix[ni][nj] = matrix[ci][cj] + 1
                queue.append((ni, nj))                
                if ni == N-1 and nj == M-1:
                    return matrix[ni][nj]

print(maze(1, 1))
