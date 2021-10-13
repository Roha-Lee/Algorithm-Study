# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def DFS(self, node, p, q, paths, path):
        if node is None: return 
        path.append(node)
        if node.val == p.val or node.val == q.val:
            paths.append(path[:])
        self.DFS(node.left, p, q, paths, path)
        self.DFS(node.right, p, q, paths, path)
        path.pop()
        
            
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        paths = []
        self.DFS(root, p, q, paths, [])
        idx = -1
        for elem1, elem2 in zip(paths[0], paths[1]):
            if not elem1.val == elem2.val:
                break
            idx +=1 
        return paths[0][idx]
        