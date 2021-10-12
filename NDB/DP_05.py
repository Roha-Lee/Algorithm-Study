t = int(input())
for _ in range(t):
    n, m = map(int, input().split())    
    raw_golds = list(map(int, input().split()))
    golds = []
    for i in range(n):
        golds.append(raw_golds[i*m:(i+1)*m])
    
    DP = [[0] * m for _ in range(n)]
    for i in range(n):
        DP[i][0] = golds[i][0]
    
    max_golds = 0
    for j in range(1, m):
        for i in range(n):
            DP[i][j] = golds[i][j] + DP[i][j-1]
            if i-1 >= 0:
                DP[i][j] = max(DP[i][j], golds[i][j] + DP[i-1][j-1])
            if i+1 < n:
                DP[i][j] = max(DP[i][j], golds[i][j] + DP[i+1][j-1])
            if max_golds < DP[i][j]:
                max_golds = DP[i][j]
    print(max_golds)