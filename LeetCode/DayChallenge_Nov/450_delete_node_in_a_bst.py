# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None: return 
        
        # Search 
        curr = root
        prev = curr
        while curr:
            if curr.val < key:
                prev = curr
                curr = curr.right
            elif curr.val > key: 
                prev = curr
                curr = curr.left
            else:
                break
        if curr is None: return root
        
        replace = curr
        if replace.right:
            replace = replace.right
            replace_prev = replace
            while replace.left:
                replace_prev = replace
                replace = replace.left
            if replace == replace_prev:
                replace.left = curr.left
                if prev.val > curr.val:
                    prev.left = replace
                elif prev.val < curr.val:
                    prev.right = replace
                else:
                    root = replace
            else:
                replace_prev.left = replace.right
                if prev.val > curr.val:
                    prev.left = replace
                elif prev.val < curr.val:
                    prev.right = replace
                else:
                    root = replace
                replace.right = curr.right
                replace.left = curr.left
        else:
            if prev.val > curr.val:
                prev.left = replace.left
            elif prev.val < curr.val:
                prev.right = replace.left
            else:
                root = replace.left
            
            
        return root