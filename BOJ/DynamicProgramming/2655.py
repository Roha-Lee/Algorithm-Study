import sys
input = sys.stdin.readline
n = int(input())
next = {i:i for i in range(1, n+1)}
DP = [0] * n
bricks = []

for i in range(1, n+1):
    area, height, weight = map(int, input().split())
    bricks.append((area, weight, height, i))

bricks = sorted(bricks, reverse=True)
for i in range(n):
    DP[i] = bricks[i][2]
    for j in range(n):
        if bricks[j][1]  > bricks[i][1] and DP[i] < DP[j] + bricks[i][2] :
            DP[i] = DP[j] + bricks[i][2]
            next[bricks[i][3]] = bricks[j][3]

cnt = 1
curr = bricks[DP.index(max(DP))][3]
paths = [str(curr)]
while next[curr] != curr:
    cnt += 1
    curr = next[curr]
    paths.append(str(curr))
print(cnt)
print('\n'.join(paths))