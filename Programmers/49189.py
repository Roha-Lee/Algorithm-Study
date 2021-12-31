from collections import defaultdict
def solution(n, edge):
    graph = defaultdict(list)
    visited = [False] * (n + 1)
    for s, d in edge:
        graph[s].append(d)
        graph[d].append(s)
    q, next_q = [1], []
    visited[1] = True
    answer = 0

    while q:
        while q:
            curr = q.pop()        
            for nb in graph[curr]:
                if visited[nb]:
                    continue
                next_q.append(nb)
                visited[nb] = True
    
        if next_q:
            answer = len(next_q)
        q, next_q = next_q, []
        
    return answer