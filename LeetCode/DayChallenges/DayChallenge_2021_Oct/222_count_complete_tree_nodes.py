# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _count(self, node, cnt=0):
        if node is None: return cnt
        cnt += 1
        if node.left:
            cnt = self._count(node.left, cnt)
        if node.right: 
            cnt = self._count(node.right, cnt)
        return cnt
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        return self._count(root)