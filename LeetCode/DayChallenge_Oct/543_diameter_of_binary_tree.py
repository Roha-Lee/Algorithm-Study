# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def DFS(self, node, paths, path):
        if node is None: return 
        if node.left is None and node.right is None: 
            path.append(node)
            paths.append(path[:])
            path.pop()
            return 
        
        path.append(node)
        self.DFS(node.left, paths, path)
        self.DFS(node.right, paths, path)
        path.pop()
        
    def get_diameter(self, path1, path2):
        idx = 0
        for let1, let2 in zip(path1, path2):
            if let1 == let2:
                idx += 1
            else:
                break
                
        return len(path1) + len(path2) - 2 * idx
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None: return 0
        paths = []
        self.DFS(root, paths, [])
        diameter = len(paths[0])-1
        for i in range(len(paths)):
            for j in range(i+1, len(paths)):
                path1, path2 = paths[i], paths[j]
                new_diameter = self.get_diameter(path1, path2) 
                if new_diameter > diameter:
                    diameter = new_diameter
                if len(path1) > diameter:
                    diameter = len(path1)-1
                if len(path2) > diameter:
                    diameter = len(path2)-1

        return diameter
                
        