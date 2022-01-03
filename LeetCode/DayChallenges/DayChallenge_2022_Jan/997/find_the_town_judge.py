from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1
        
        graph = defaultdict(int)
        r_graph = defaultdict(int)
        for src, dst in trust:
            graph[dst] += 1
            r_graph[src] += 1
        for person in range(1, n+1): 
            if(graph[person] == n-1 and r_graph[person] == 0):
                return person
        return -1