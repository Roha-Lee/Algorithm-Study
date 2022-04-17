# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        result = []
        def inorder(node):
            if node is None: return 
            inorder(node.left)
            result.append(node)
            inorder(node.right)
        inorder(root)
        for i in range(1, len(result)):
            result[i-1].right = result[i]
            result[i-1].left = None
        result[-1].left = None
        return result[0]