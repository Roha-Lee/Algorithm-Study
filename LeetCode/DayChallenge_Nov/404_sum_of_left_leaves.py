# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, results, direction='root'):
        if node is None: 
            return 
        if direction == 'left' and node.left is None and node.right is None:
            results.append(node.val)
            return 
        if node.left:
            self.dfs(node.left, results, 'left')
        if node.right: 
            self.dfs(node.right, results, 'right')
        
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        results = []
        self.dfs(root, results)
        return sum(results)
        
        