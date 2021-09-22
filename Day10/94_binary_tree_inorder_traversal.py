# Recursive solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def _traversal(result, node):
            if node is None: return
            _traversal(result, node.left)
            result.append(node.val)
            _traversal(result, node.right)
        result = []
        _traversal(result, root)
        return result

# Iterative solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        if root is None: return 
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right
        return result

# iterative solution with visited flag 
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return 
        visited = set()
        stack = [root]
        result = []
        node = root
        while stack or node:
            if node.left and not node.left in visited:
                node = node.left
                stack.append(node)
            else:
                if not node in visited:
                    result.append(node.val)
                    visited.add(node)
                if node.right and not node.right in visited:
                    node = node.right
                    stack.append(node)
                else:
                    if stack:
                        node = stack.pop()
                    else:
                        node = None
        return result
                
                
                
                
                
                
                
                
                
                
                