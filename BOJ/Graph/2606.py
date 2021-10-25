from collections import deque 
import sys
input = sys.stdin.readline
n = int(input())
e = int(input())
graph = {i:[] for i in range(1, n+1)}

for _ in range(e):
    src, dst = map(int, input().split())
    graph[src].append(dst)
    graph[dst].append(src)

def bfs(start=1):
    visited = [False] * (n+1)
    q = deque([start])
    visited[start] = True
    cnt = 0
    while q:
        curr = q.popleft()
        for nb in graph[curr]:
            if not visited[nb]:
                q.append(nb)
                visited[nb] = True
                cnt += 1
    return cnt
    
print(bfs())