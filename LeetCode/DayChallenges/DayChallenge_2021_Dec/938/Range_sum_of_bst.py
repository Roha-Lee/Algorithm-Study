# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = 0
    def preorder(self, low, high, node):
        if node is None: 
            return None
        if low <= node.val <= high:
            self.answer += node.val
        self.preorder(low, high, node.left)
        self.preorder(low, high, node.right)
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.preorder(low, high, root)
        return self.answer
        