from disjoint_set import DisjointSet
# undirected graph 
graph1 = {
    1:[2,3],
    2:[3,1],
    3:[1,2]
}
graph2 ={
    1:[2,3],
    2:[1], 
    3:[1]
}
graph = graph1
cycle = False
visited = {node:False for node in graph.keys()}
dset = DisjointSet(graph.keys())
for src in graph.keys():
    for dst in graph[src]:
        if visited[dst]:
            continue
        if dset.find(src) == dset.find(dst):
            cycle = True
            break
        else:
            dset.union(src, dst)
    visited[src] = True
# print(cycle)

# directed graph 
graph1 = {
    1:[2,3],
    2:[3,1],
    3:[1,2]
}
graph2 ={
    1:[2,3],
    2:[1,3], 
    3:[]
}
graph3 = {
    1:[3,4,6],
    2:[],
    3:[2],
    4:[3],
    5:[4],
    6:[5]
}
def _check_cycle_from_node(history, graph, node):
    if node in history:
        return True
    
    history.append(node)
    for next in graph[node]:
        if _check_cycle_from_node(history, graph, next):
            return True
    history.pop()
    return False
    
def check_cycle(graph):
    for node in graph.keys():
        if _check_cycle_from_node([], graph, node):
            return True
    return False
        
print(check_cycle(graph3))