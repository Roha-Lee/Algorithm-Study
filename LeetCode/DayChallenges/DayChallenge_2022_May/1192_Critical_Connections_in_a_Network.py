from collections import defaultdict
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.rank = []
        self.answer = []

    def dfs(self, node = 0, rank = 0, parent = None):
        if self.rank[node] != -1: return
        self.rank[node] = rank
        for neighbor in self.graph[node]:
            if neighbor == parent: continue
            if self.rank[neighbor] == -1:
                self.dfs(neighbor, rank + 1, node)
            self.rank[node] = min(self.rank[neighbor], self.rank[node])
            if self.rank[neighbor] > rank:
                self.answer.append([node, neighbor])
        
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        for u, v in connections:
            self.graph[u].append(v)
            self.graph[v].append(u)
        self.rank = [-1 for _ in range(n)]
        self.dfs()    
        return self.answer