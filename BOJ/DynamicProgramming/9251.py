import sys 
input = sys.stdin.readline
str1 = input().rstrip()
str2 = input().rstrip()
DP = [[0] * (len(str1)+1) for _ in range(len(str2)+1)]
for i in range(1, len(str2) + 1):
    for j in range(1, len(str1) + 1):
        if str1[j-1] == str2[i-1] :
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])
print(DP[-1][-1])