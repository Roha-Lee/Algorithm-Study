# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _merge(self, n1, n2, prev):
        val1 = val2 = 0
        if n1.val == 10001 and n2.val == 10001:
            if prev.left == n1:
                prev.left = None
            elif prev.right == n1:
                prev.right = None
            return 
        val1 = 0 if n1.val == 10001 else n1.val
        val2 = 0 if n2.val == 10001 else n2.val
        n1.val = val1 + val2
        
        if n1.left is None: 
            n1.left = TreeNode(10001)
        if n2.left is None: 
            n2.left = TreeNode(10001)
        self._merge(n1.left, n2.left, n1)
        
        if n1.right is None: 
            n1.right = TreeNode(10001)
        if n2.right is None:
            n2.right = TreeNode(10001)
        self._merge(n1.right, n2.right, n1)

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None: 
            return root1
        self._merge(root1, root2, root1)
        return root1
        