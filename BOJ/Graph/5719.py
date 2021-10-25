import sys 
import heapq
from collections import deque

def dijkstra():
    nodes[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q: 
        dist, src = heapq.heappop(q)
        if dist > nodes[src]:
            continue
        for dst, cost in graph[src].items():
            if nodes[dst] > dist + cost:
                nodes[dst] = dist + cost
                heapq.heappush(q, (nodes[dst], dst))
            
def remove_paths():
    q = deque()
    q.append((nodes[end], end))
    while q:
        cost, curr = q.popleft()
        if curr == start:
            continue
        
        for dst, weight in reverse_graph[curr]:
            if cost - weight == nodes[dst]:
                if (dst, curr) not in removed:
                    q.append((nodes[dst], dst))
                    removed.append((dst, curr))

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    start, end = map(int, input().split())
    graph = {i:dict() for i in range(n)}
    reverse_graph = {i:[] for i in range(n)}
    
    for _ in range(m):
        u, v, p = map(int, input().split())
        graph[u][v] = p
        reverse_graph[v].append((u, p))
    nodes = [float('inf')] * n
    dijkstra()
    removed = []
    remove_paths()
    for src, dst in removed:
        del graph[src][dst]
    nodes = [float('inf')] * n
    dijkstra()

    if nodes[end] == float('inf'):
        print(-1)
    else:
        print(nodes[end])