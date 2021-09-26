# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None: 
            root = TreeNode(val)
            return root
        curr = root
        while curr:
            if curr.val < val:
                if curr.right: 
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    return root
            else:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    return root