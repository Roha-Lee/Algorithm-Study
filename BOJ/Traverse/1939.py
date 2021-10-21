from collections import deque
import sys 
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = {node:dict() for node in range(1, n+1)}

_min = 0
_max = 1000000000
for _ in range(m):
    a, b, c = map(int, input().split())
    _min = min(_min, c)
    _max = max(_max, c)
    if b in graph[a]:
        graph[a][b] =  max(graph[a][b], c)
    else:
        graph[a][b] = c
    if a in graph[b]:
        graph[b][a] =  max(graph[b][a], c)
    else:
        graph[b][a] = c
start, end = map(int, input().split())

def can_reach(weight, start, end):
    queue = deque()
    visited = [False] * (n+1)
    queue.append(start)
    visited[start] = True
    while queue:
        curr = queue.popleft()
        if curr == end: 
            return True
        for node in graph[curr]:
            if not visited[node] and graph[curr][node] >= weight:
                queue.append(node)
                visited[node] = True
            
    return False

best = 0
while _min <= _max:
    mid = (_min + _max) // 2
    visited = [False] * (n+1)
    visited[start] = True
    if can_reach(mid, start, end):
        best = mid
        _min = mid + 1
    else:
        _max = mid - 1
print(best)