import sys 
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())

graph = {node:[] for node in range(1, n+1)}
for _ in range(m):
    pre, post = map(int, input().split())
    graph[pre].append(post)

indegree = {node:0 for node in graph}
for nodes in graph.values():
    for v in nodes:
        indegree[v] += 1
q = []

for k, v in indegree.items():
    if v == 0:
        heapq.heappush(q, k)
while q:
    node = heapq.heappop(q)
    print(node, end= ' ')
    for v in graph[node]:
        indegree[v] -= 1
        if indegree[v] == 0:
            heapq.heappush(q, v)
            
print()