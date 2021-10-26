import sys 
import heapq
input = sys.stdin.readline
n = int(input())
info = []
for _ in range(n):
    deadline, cup = map(int, input().split())
    info.append((deadline, cup))

info = sorted(info)

q = []
for deadline, cup in info:
    heapq.heappush(q, cup)
    if deadline < len(q):
        heapq.heappop(q)    

print(sum(q))
    