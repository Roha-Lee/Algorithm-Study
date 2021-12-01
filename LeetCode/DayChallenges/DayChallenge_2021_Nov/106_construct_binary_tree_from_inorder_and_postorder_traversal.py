# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return 
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root = TreeNode(postorder[-1])
        cut_idx = inorder.index(postorder[-1])
        
        left_root = self.buildTree(inorder[:cut_idx], postorder[:cut_idx])
        right_root = self.buildTree(inorder[cut_idx+1:], postorder[cut_idx:-1])
        root.left, root.right = left_root, right_root
        
        return root