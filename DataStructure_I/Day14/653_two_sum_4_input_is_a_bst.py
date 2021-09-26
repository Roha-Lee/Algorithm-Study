# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        history = set()
        def traversal(history, node):
            if node is None: return 
            history.add(node.val)
            traversal(history, node.left)
            traversal(history, node.right)
        def findK(node, history, k):
            if node is None: return
            query = k - node.val
            if query == node.val or query not in history:
                return findK(node.left, history, k) or findK(node.right,history, k)
            return True
        traversal(history, root)
        return findK(root, history, k)