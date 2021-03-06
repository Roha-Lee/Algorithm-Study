import sys 
input = sys.stdin.readline

n, k = map(int, input().split())

DP = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1, n+1):
    weight, value = map(int, input().split())
    for j in range(1, k+1):
        if j < weight:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(DP[i-1][j-weight] + value, DP[i-1][j])

print(DP[-1][-1])