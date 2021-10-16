import sys 
input = sys.stdin.readline
test_num = int(input())

def find_parent(parents, p):
    if p != parents[p]:
        parents[p] = find_parent(parents, parents[p])
    return parents[p]
    
for _ in range(test_num):
    rel_num = int(input())
    parents = dict()
    groups = dict()
    for _ in range(rel_num):
        p1, p2 = input().rstrip().split()
        if not p1 in parents:
            parents[p1] = p1
            groups[p1] = 1
        else:
            p1 = find_parent(parents, p1)
        if not p2 in parents:
            parents[p2] = p2
            groups[p2] = 1
        else:
            p2 = find_parent(parents, p2)

            
        if p1 == p2: 
            print(groups[p2])
            continue
        parents[p1] = p2
        groups[p2] += groups[p1]
        groups[p1] = groups[p2]
        print(groups[p2])
        