# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, node, result, k):
        if node is None: 
            return 
        self.DFS(node.left, result, k)
        if len(result) < k:
            result.append(node.val)
        self.DFS(node.right, result, k)

        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []        
        self.DFS(root, result, k)
        return result[-1]
        