import math
import sys
input = sys.stdin.readline

def get_distance(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    return math.sqrt((a * a) + (b * b))
class DisjointSet:
    def __init__(self, n):
        self.parent = {i:i for i in range(1, n+1)}

    def find(self, n):
        if not self.parent[n] == n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a < b:
            self.parent[b] = a
        else:
            self.parent[a] = b

edges = []
locations = []
n, m = map(int, input().split())
network = DisjointSet(n)
for _ in range(n):
    x, y = map(int, input().split())
    locations.append((x, y))

length = len(locations)
for i in range(length - 1):
    for j in range(i + 1, length):
        edges.append((i + 1, j + 1, get_distance(locations[i], locations[j])))


for i in range(m):
    a, b = map(int, input().split())
    network.union(a, b)

edges.sort(key=lambda data: data[2])

result = 0
for a, b, cost in edges:
    if network.find(a) != network.find(b):
        network.union(a, b)
        result += cost

print("%0.2f" % result)