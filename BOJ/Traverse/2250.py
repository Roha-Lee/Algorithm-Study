import sys 
input = sys.stdin.readline
n = int(input())
tree = {node:[] for node in range(1, n+1)}
root_candidates = set(range(1, n+1))
for _ in range(n):
    node, left, right = map(int, input().split())
    tree[node].append(left)
    tree[node].append(right)
    if left != -1:
        root_candidates.remove(left)
    if right != -1:
        root_candidates.remove(right)

def inorder(node, level=1, loc=1):
    if tree[node][0] != -1:
        inorder(tree[node][0], level + 1, loc)
    
    traverse.append(node)
    if not level in width_map:
        width_map[level] = [n, 0]
    loc = len(traverse)
    width_map[level][0] = min(width_map[level][0], loc)
    width_map[level][1] = max(width_map[level][1], loc)
    
    if tree[node][1] != -1:
        inorder(tree[node][1], level + 1, loc)

root = root_candidates.pop()
traverse = []
width_map = dict()
inorder(root)
max_width = 0
max_lv = 0
for i in range(1, len(width_map)+1):
    if max_width < width_map[i][1] - width_map[i][0] + 1:
        max_lv = i
        max_width = width_map[i][1] - width_map[i][0] + 1
print(max_lv, max_width)  
