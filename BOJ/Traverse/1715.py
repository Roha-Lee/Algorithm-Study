import sys 
import heapq
input = sys.stdin.readline
n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))
cnt = 0
while q:
    hand1 = heapq.heappop(q)
    if q:
        hand2 = heapq.heappop(q)
        cnt += hand1 + hand2
        if not q: 
            break
        else:
            heapq.heappush(q, hand1+hand2)
print(cnt)