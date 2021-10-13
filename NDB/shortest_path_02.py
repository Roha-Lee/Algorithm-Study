# Floyd Warshall
graph = {
  1:[(2, 4), (4, 6)],
  2:[(1, 3), (3, 7)],
  3:[(1, 5), (4, 4)],
  4:[(3, 2)]
}
N = len(graph)
DP = [[float("Inf")] * (N+1) for _ in range(N+1)]
for src in range(1,N+1):
    DP[src][src] = 0
    neighbors = graph[src]
    for node, weight in neighbors:
        DP[src][node] = weight
for inter in range(1, N+1):
    for src in range(1, N+1):
        for dst in range(1, N+1):
            if src == dst: 
                continue            
            DP[src][dst] = min(DP[src][dst], DP[src][inter] + DP[inter][dst])
from pprint import pprint 
pprint(DP)