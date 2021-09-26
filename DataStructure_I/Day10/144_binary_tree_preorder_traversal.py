# Recursive solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def _traversal(result, node):
            if node is None: 
                return 
            result.append(node.val)
            if node.left:
                _traversal(result, node.left)
            if node.right:
                _traversal(result, node.right)
            return 
        _traversal(result, root)
        return result

# Iterative solution

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root
        if not curr:
            return 
        stack.append(curr)
        while len(stack):
            result.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                curr = curr.left
            else:
                curr = stack.pop()
        return result

# iterative solution with visited flag.
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return
        
        result = [root.val]
        stack = [root]
        visited = {root}
        node = root
        while stack or node:
            if node.left and not node.left in visited:
                node = node.left
                stack.append(node)
                result.append(node.val)
                visited.add(node)
            elif node.right and not node.right in visited:
                node = node.right
                stack.append(node)
                result.append(node.val)
                visited.add(node)
            else:
                if stack:
                    node = stack.pop()
                else:
                    node = None
                
        return result
        
        