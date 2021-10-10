# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        result = []
        stack = [root]
        toggle = True
        
        while stack:
            current_row = []
            current_queue = []
            while stack:
                node = stack.pop()
                current_queue.append(node)
                
            while current_queue:
                node = current_queue.pop(0)
                if toggle:
                    if node.left:
                        stack.append(node.left)
                    if node.right: 
                        stack.append(node.right)
                else:
                    if node.right: 
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
                current_row.append(node.val)     
            toggle = not toggle
            result.append(current_row)
        return result

        
        
        