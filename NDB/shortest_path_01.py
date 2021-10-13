import heapq
# Dijkstra's algorithm
graph = { # node : (dest, weight)
  1: [(2, 2), (4, 1), (3, 5)],
  2: [(4, 2), (3, 3)],
  3: [(2, 3), (6, 5)], 
  4: [(3, 3), (5, 1)], 
  5: [(3, 1), (6, 2)], 
  6: []
}
start_node = 1

TABLE = {node:(float("Inf"), None) for node in graph.keys()}
TABLE[start_node] = (0, start_node)
pri_q = []
heapq.heappush(pri_q, (TABLE[start_node], start_node))
while pri_q:
    (distance, origin), node = heapq.heappop(pri_q)
    if TABLE[node][0] < distance:
        continue
    neighbors = graph[node]
    for dest, weight in neighbors:
        if TABLE[dest][0] > distance + weight:
            TABLE[dest] = (distance + weight, node)
            heapq.heappush(pri_q, (TABLE[dest], dest))

# 모든 목적지까지 거리, 경로 출력 
for target in range(1, 7):
    dest = target
    distance = TABLE[target][0]
    path = str(target)
    while target != TABLE[target][1]:
        target = TABLE[target][1]
        path = path + '→' + str(target)
    print(f'{dest}\ndistance: {distance}, path: {path[::-1]}\n')