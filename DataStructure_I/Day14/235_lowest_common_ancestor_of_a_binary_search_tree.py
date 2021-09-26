# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        prev = curr
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)
        stack = []
        while stack or curr:
            if min_val <= curr.val and curr.val <= max_val:
                break
            if curr.left:
                if curr.right: 
                    stack.append(curr.right)
                curr = curr.left    
            else:
                if stack:
                    curr = stack.pop()
                else:
                    curr = None
        return curr




