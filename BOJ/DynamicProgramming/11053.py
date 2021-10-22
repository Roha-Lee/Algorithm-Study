import sys 
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
DP = [0] * n
DP[0] = 1
for i in range(1, n):
    max_val = 0
    for j in range(i):
        if nums[i] > nums[j]:
            max_val = max(max_val, DP[j])
    DP[i] = max_val + 1
print(max(DP))