import sys 
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
q = deque([n])
DP = [0] * 100001

while q:
    curr = q.popleft()
    if curr == k:
        break 
    for new_val in (curr - 1, curr + 1, 2 * curr):
        if 0 <= new_val and new_val <= 100000 and DP[new_val] == 0:
            DP[new_val] = DP[curr] + 1
            q.append(new_val)

print(DP[k])

