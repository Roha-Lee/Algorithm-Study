import heapq
import sys 
from disjoint_set import DisjointSet

input = sys.stdin.readline

N, M = map(int, input().split())
dset = DisjointSet(list(range(1, N+1)))
graph = [[float("Inf")] * (N+1) for _ in range(N+1)]
edges = []
for _ in range(M):
    src, dst, weight = map(int, input().split())
    graph[src][dst] = weight
    graph[dst][src] = weight
    heapq.heappush(edges, (weight, src, dst))

min_span_tree = {node:[] for node in range(1, N+1)}
total_weight = 0
while edges:
    weight, src, dst = heapq.heappop(edges)
    if not dset.find(src) == dset.find(dst):
        dset.union(src, dst)
        min_span_tree[src].append(dst)
        min_span_tree[dst].append(src)
        total_weight += weight
print(total_weight)
print(min_span_tree)
    

