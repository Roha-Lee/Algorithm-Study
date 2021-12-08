# Definition for a binary tree node.
# from typing import * 
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

        left_sum, left_tilt_sum = self.dfs(node.left)
        right_sum, right_tilt_sum = self.dfs(node.right)
        return left_sum + right_sum + node.val, left_tilt_sum + right_tilt_sum + abs(left_sum - right_sum)
            
    def findTilt(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[1]
        