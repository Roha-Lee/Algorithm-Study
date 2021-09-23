# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def _max_depth(node, depth):
            if node is None: return depth - 1
            max_depth = depth
            if node.left: 
                new_depth = _max_depth(node.left, depth + 1)
                max_depth = max_depth if max_depth > new_depth else new_depth
            if node.right:
                new_depth = _max_depth(node.right, depth + 1)
                max_depth = max_depth if max_depth > new_depth else new_depth
            return max_depth
        return _max_depth(root, 1)