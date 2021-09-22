# Recursive solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def _traversal(result, node):
            if node is None: return
            _traversal(result, node.left)
            _traversal(result, node.right)
            result.append(node.val)
        result = []
        _traversal(result, root)
        return result
        
# Iterative solution
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root is None: return 
#         curr = root
#         prev = None
#         stack = []
#         result = []
#         while stack or curr: 
#             if curr: 
#                 stack.append(curr)
#                 curr = curr.left
#             else:
#                 top = stack[-1]
#                 if top.right and not top.right == prev:
#                     curr = top.right
#                 else:
#                     result.append(top.val)
#                     prev = top
#                     stack.pop()
#         return result

# iterative solution with visited flag
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
                if node.right and not node.right in visited:
                    stack.append(node)
                    node = node.right
                else:
                    if not node in visited:
                        result.append(node.val)
                        visited.add(node)
                    else:
                        if stack: 
                            node = stack.pop()
                        else:
                            node = None

        return result
                
                
                
    