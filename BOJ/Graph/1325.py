from collections import deque
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(node):
    visited = [False] * (n+1)
    q = deque([node])
    visited[node] = True
    cnt = 1
    while q:
        curr = q.popleft()
        for nb in graph[curr]:
            if not visited[nb]:
                visited[nb] = True
                q.append(nb)
                cnt += 1
    return cnt

max_value = -1
result = []
for i in range(1, n+1):
    count = bfs(i)
    if count > max_value:
        result = [i]
        max_value = count
    elif count == max_value:
        result.append(i)
for i in result:
    print(i, end=' ')
print()