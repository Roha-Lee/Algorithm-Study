from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = deque([(0, [0])])
        results = []
        while q:
            curr_node, path = q.popleft()
            if curr_node == len(graph) - 1:
                results.append(path[:])
                continue
            for next_node in graph[curr_node]:
                path.append(next_node)
                q.append((next_node, path[:]))
                path.pop()
                
        return results
        