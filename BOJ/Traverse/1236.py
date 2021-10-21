import sys 
input = sys.stdin.readline
n, m = map(int, input().split())
castle = [[0 if curr == '.' else 1 for curr in input().rstrip()] for _ in range(n)]

empty_rows = [True for i in range(n)]
empty_cols = [True for i in range(m)]
for i in range(n):
    for j in range(m):
        if castle[i][j] == 1:
            empty_cols[j] = False
            empty_rows[i] = False
print(max(sum(empty_rows), sum(empty_cols)))
