import sys 
input = sys.stdin.readline
n = int(input())
tree = dict()
for _ in range(n):
    node, left, right = input().rstrip().split()
    tree[node] = (left, right)

def preorder(tree, node):
    print(node, end='')
    if not tree[node][0] == '.':
        preorder(tree, tree[node][0])
    if not tree[node][1] == '.':
        preorder(tree, tree[node][1])

def inorder(tree, node):
    if not tree[node][0] == '.':
        inorder(tree, tree[node][0])
    print(node, end='')
    if not tree[node][1] == '.':
        inorder(tree, tree[node][1])

def postorder(tree, node):
    if not tree[node][0] == '.':
        postorder(tree, tree[node][0])
    if not tree[node][1] == '.':
        postorder(tree, tree[node][1])
    print(node, end='')

preorder(tree, 'A')
print()
inorder(tree, 'A')
print()
postorder(tree, 'A')
print()