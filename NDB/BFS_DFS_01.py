N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input())))

def ice(i, j):
    if not (i >= 0 and i < N and j >= 0 and j < M):
        return False
    if matrix[i][j] == 0:
        matrix[i][j] = 1
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in moves:
            ice(i + di, j + dj)
        return True
    return False

result = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if ice(i, j):
            result += 1
print(result)