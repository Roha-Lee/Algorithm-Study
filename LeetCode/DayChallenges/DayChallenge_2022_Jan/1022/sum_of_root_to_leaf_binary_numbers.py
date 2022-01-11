# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binary_dfs(self, node, temp, results):
        if node is None:
            return
        if node.left is None and node.right is None:
            results.append(temp + node.val)
            return 
        
        self.binary_dfs(node.left, (temp + node.val) << 1, results)
        self.binary_dfs(node.right, (temp + node.val) << 1, results)
        
        
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        results = []
        self.binary_dfs(root, 0, results)
        return sum(results)