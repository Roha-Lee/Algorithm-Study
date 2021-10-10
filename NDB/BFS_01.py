from collections import deque
def BFS(graph, v, visited):
    visited[v] = True    
    queue = deque([v])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
if __name__ == '__main__':
    graph = {
        1: [2, 3, 8], 
        2: [1, 7],
        3: [1, 4, 5], 
        4: [3, 5], 
        5: [3, 4], 
        6: [7],
        7: [2, 6, 8], 
        8: [1, 7]
    }
    visited = [False]* (len(graph) + 1)
    BFS(graph, 1, visited)