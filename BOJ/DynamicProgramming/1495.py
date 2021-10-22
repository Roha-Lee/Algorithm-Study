# import sys 
# input = sys.stdin.readline
# n, s, m = map(int, input().split())
# volumes = list(map(int, input().split()))
# def DFS(s, i, m, volumes, result):
#     if s > m or 0 > s:
#         return
#     if i == n:
#         result.append(s)
#         return 
    
#     DFS(s+volumes[i], i+1, m, volumes, result)    
#     DFS(s-volumes[i], i+1, m, volumes, result)

# result = []
# DFS(s, 0, m, volumes, result)
# if result:
#     print(max(result))
# else:
#     print(-1)

import sys 
input = sys.stdin.readline
n, s, m = map(int, input().split())
volumes = list(map(int, input().split()))
DP = [[False] * (m+1) for _ in range(n+1)]
DP[0][s] = True
for i in range(1, n+1):
    volume = volumes[i-1]
    for j in range(m+1):
        if DP[i-1][j]:
            if j - volume >= 0:
                DP[i][j-volume] = True
            if j + volume <= m:
                DP[i][j+volume] = True
result = -1
for i in range(m, -1, -1):
    if DP[n][i]:
        result = i
        break
print(result)

