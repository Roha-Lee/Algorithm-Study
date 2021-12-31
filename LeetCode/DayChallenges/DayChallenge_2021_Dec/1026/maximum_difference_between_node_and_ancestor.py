# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_diff = 0
    def dfs(self, prev_min, prev_max, node):
        if node is None:
            return 
        self.max_diff = max(self.max_diff, 
                            abs(prev_max - node.val),
                            abs(prev_min - node.val))
        next_max = max(prev_max, node.val)
        next_min = min(prev_min, node.val)
        self.dfs(next_min, next_max, node.left)
        self.dfs(next_min, next_max, node.right)
        
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.dfs(root.val, root.val, root)
        return self.max_diff