import sys 
import heapq
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, dep, virus = map(int, input().split())
    graph = {i:[] for i in range(1, n+1)}
    dist = [float('inf')] * (n+1)
    dist[virus] = 0
    for _ in range(dep):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    q = []
    heapq.heappush(q, (0, virus))
    while q: 
        cur_dist, src = heapq.heappop(q)
        if cur_dist > dist[src]:
            continue
        for dst, weight in graph[src]:
            if dist[dst] > dist[src] + weight:
                dist[dst] = dist[src] + weight
                heapq.heappush(q, (dist[dst], dst))
    max_dist = 0
    cnt = 0
    for d in dist:
        if d == float('inf'):
            continue
        else:
            cnt += 1
            if max_dist < d:
                max_dist = d
    print(cnt, max_dist)
    
        
