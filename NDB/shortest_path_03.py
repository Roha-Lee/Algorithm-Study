import heapq

N, M, C = map(int, input().split())
graph = [[float("Inf")] * (N+1) for _ in range(N+1)]
for _ in range(M):
    src, dest, time = map(int, input().split())
    graph[src][dest] = time

paths = [float("Inf")] * (N+1)
paths[C] = 0

q = []
heapq.heappush(q, (0, C))
while q:
    dist, node = heapq.heappop(q)
    for dst in range(1, N+1):
        if graph[src][dst] == float("Inf"):
            continue
        if paths[dst] < dist + graph[src][dst]:
            continue
        paths[dst] = dist + graph[src][dst]
        heapq.heappush(q, (paths[dst], dst))

longest_time = 0
num_country = 0
for path in paths[1:]:
    if path == float("Inf") or path == 0:
        continue
    if path > longest_time:
        longest_time = path
    num_country += 1

print(num_country, longest_time)