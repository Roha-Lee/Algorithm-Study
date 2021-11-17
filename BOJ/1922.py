import sys 

# Kruskal's algorithm

class DisjointSet:
    def __init__(self, n):
        self.parents = {i:i for i in range(1, n+1)}
        self.heights = {i:0 for i in range(1, n+1)}
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y: 
            if self.heights[x] < self.heights[y]:
                self.parents[y] = self.parents[x]
            else:
                self.parents[x] = self.parents[y]

    def find(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

def get_mst_cost(n, costs):
    disj_set = DisjointSet(n)
    costs = sorted(costs, key = lambda x: x[2])
    total_cost = 0
    for src, dst, cost in costs:
        if disj_set.find(src) != disj_set.find(dst):
            total_cost += cost
            disj_set.union(src, dst)
    return total_cost

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    
    costs = []
    for _ in range(m):
        src, dst, cost = map(int, input().split())
        costs.append((src, dst, cost))
    
    print(get_mst_cost(n, costs))
