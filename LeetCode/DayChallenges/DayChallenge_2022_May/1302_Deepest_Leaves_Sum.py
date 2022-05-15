# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        next_q = []
        while q:
            result = 0
            while q:
                curr = q.pop()
                result += curr.val
                if curr.left:
                    next_q.append(curr.left)
                if curr.right:
                    next_q.append(curr.right)
            q, next_q = next_q, []
        return result