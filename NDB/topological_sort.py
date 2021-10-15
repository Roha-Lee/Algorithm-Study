from collections import deque
graph = {
    1:[2, 5],
    2:[3, 6], 
    3:[4], 
    4:[7],
    5:[6], 
    6:[4],
    7:[]
}

def topological_sort(graph):
    indegree = {node:0 for node in graph}
    for nodes in graph.values():
        for v in nodes:
            indegree[v] += 1
    q = deque()
    for k, v in indegree.items():
        if v == 0:
            q.append(k)
    while q:
        node = q.popleft()
        print(node, end= ' ')
        for v in graph[node]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
        
    
topological_sort(graph)