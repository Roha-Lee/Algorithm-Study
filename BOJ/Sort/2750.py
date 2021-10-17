import sys 
import heapq
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]
heapq.heapify(nums)
for _ in range(n):
    print(heapq.heappop(nums))
