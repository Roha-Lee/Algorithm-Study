from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1: return [0]
        graph = defaultdict(set)
        for src, dst in edges:
            graph[src].add(dst)
            graph[dst].add(src)
            
        q = deque()
        for node in graph:
            if len(graph[node]) == 1:
                q.append(node)
        
        result = None
        next_queue = []
        while q:
            result = list(q)
            next_queue = deque()
            while q:
                curr = q.popleft()
                for neighbor in graph[curr]:
                    graph[neighbor].remove(curr)
                    if len(graph[neighbor]) == 1:
                        next_queue.append(neighbor)
            q = next_queue

        return result

            
        