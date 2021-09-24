# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path_sum_result = []
        def _path_sum(result, node, target_sum):
            if node is None: return
            if node.left is None and node.right is None:
                result.append(target_sum - node.val)
                return 
            _path_sum(result, node.left, target_sum - node.val)
            _path_sum(result, node.right, target_sum - node.val)
        _path_sum(path_sum_result, root, targetSum)
        return 0 in path_sum_result
        