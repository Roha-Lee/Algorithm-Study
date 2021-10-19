import sys
input = sys.stdin.readline
n = int(input())
pos_dict = [0] * 1000001
neg_dict = [0] * 1000001
for _ in range(n):
    num = int(input())
    if num >= 0:
        pos_dict[num] += 1
    else:
        neg_dict[-num] += 1
for num in range(1000000, -1, -1):
    if neg_dict[num] > 0:
        print(-num)
for num in range(1000001):
    if pos_dict[num] > 0:
        print(num)

# SOL2
# import sys
# input = sys.stdin.readline
# n = int(input())
# nums = [int(input()) for _ in range(n)]
# for num in sorted(nums):
#     print(num)