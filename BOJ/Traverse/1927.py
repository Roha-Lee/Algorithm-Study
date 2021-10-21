import sys 
import heapq
input = sys.stdin.readline
n = int(input())
q = []
for _ in range(n):
    _in = int(input())
    if _in == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, _in)
