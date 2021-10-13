N, M = map(int, input().split())
graph = [[float('Inf')] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    graph[i][i] = 0
for _ in range(M):
    src, dst = map(int, input().split())
    graph[src][dst] = 1
    graph[dst][src] = 1
X, K = map(int, input().split())

for inter in range(1, N+1):
    for src in range(1, N+1):
        for dst in range(1, N+1):
            graph[src][dst] = min(graph[src][dst], graph[src][inter] + graph[inter][dst])
total_dist = graph[1][K] + graph[K][X]
from pprint import pprint 

if total_dist == float("Inf"):
    print(-1)
else:
    print(total_dist)
