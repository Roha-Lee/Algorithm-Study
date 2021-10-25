import sys 
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}

for _ in range(m):
    src, dst = map(int, input().split())
    graph[src].append(dst)
    graph[dst].append(src)

for node in graph:
    graph[node] = sorted(graph[node])

def dfs(graph, root, visited):
    print(root, end=' ')
    for neighbor in graph[root]:
        if not visited[neighbor]:
            visited[neighbor] = True
            dfs(graph, neighbor, visited)
        
def bfs(graph, root):
    q = deque([root])
    visited = [False] * (n+1)
    while q:
        curr = q.popleft()
        if visited[curr]:
            continue
        visited[curr] = True
        print(curr, end = ' ')
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                q.append(neighbor)
                 
visited = [False] * (n+1)    
visited[v] = True
dfs(graph, v, visited)
print()
bfs(graph, v)
print()