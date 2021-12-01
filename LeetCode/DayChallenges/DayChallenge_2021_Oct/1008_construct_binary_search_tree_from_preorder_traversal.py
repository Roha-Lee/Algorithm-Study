# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        root = TreeNode(preorder[0])
        mid = 0
        for i in range(1, len(preorder)):
            if preorder[i] > preorder[mid]:
                mid = i
                break
        left = preorder[1:mid]
        right = preorder[mid:]
        if mid == 0:
            left = preorder[1:]
            right = []
                
        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)
        return root
        