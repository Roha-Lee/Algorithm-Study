class DisjointSet:
    def __init__(self, nodes):
        # self.nodes = {node:{node} for node in nodes}
        self.parents = {node:node for node in nodes}
        # self.indices = {node:0 for node in nodes}
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a < b:
            self.parents[b] = a
        else:
            self.parents[a] = b
        # if self.indices[a] < self.indices[b]:
        #     self.parents[a] = self.find(b)
        # elif self.indices[a] > self.indices[b]:
        #     self.parents[b] = self.find(a)
        # else:
        #     self.indices[a] += 1
        #     self.parents[b] = self.find(a)
            
        # union_set = self.nodes[a].union(self.nodes[b])
        # self.nodes[a] = union_set
        # self.nodes[b] = union_set

    def find(self, a):
        if a == self.parents[a]:
            return a
        self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

if __name__ == '__main__':
    nodes = [1,2,3,4,5,6]
    dset = DisjointSet(nodes)
    for i in range(1, 7):
        print(dset.find(i), end=' ')
    dset.union(1,2)
    dset.union(5,6)
    dset.union(3,5)
    print()
    for i in range(1, 7):
        print(dset.find(i), end=' ')
    
