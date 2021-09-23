# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def _is_symmetric(left, right):
            if left is None and right is None: 
                return True
            elif left is None and right:
                return False
            elif right is None and left:
                return False 
    
            if left.val == right.val:
                return _is_symmetric(left.left, right.right) and _is_symmetric(left.right, right.left)
            else:
                return False
        return _is_symmetric(root.left, root.right)

# inorder Traversal로 문제를 해결하려고 했는데 [1, 2, 2, 2, null, 2, null]에서 막혀버렸다. 