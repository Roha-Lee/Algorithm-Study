# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if node is None:
            return 0, 0
        if node.left is None and node.right is None:
            return node.val, 0
        
        left_child = self.dfs(node.left)
        right_child = self.dfs(node.right)
        
        return  node.val + left_child[1] + right_child[1], \
                max(left_child) + max(right_child)
    
    def rob(self, root: Optional[TreeNode]) -> int:
        wo_curr, w_curr = self.dfs(root)
        return max(wo_curr, w_curr)