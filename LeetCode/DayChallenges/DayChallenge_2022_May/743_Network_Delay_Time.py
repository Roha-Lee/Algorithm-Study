from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        dist = defaultdict(int)
        
        q = [(0, k)]
        for u, v, w in times:
            graph[u].append((v, w))
        
        while q:
            time, node = heappop(q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heappush(q, (alt, v))
        print(dist)
        if len(dist) == n:
            return max(dist.values())
        return -1