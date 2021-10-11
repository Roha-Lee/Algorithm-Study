# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return 
        queue = deque([root])
        candidate = deque()
        result = []
        while queue:
            curr = queue.popleft()
            if curr.left:
                candidate.append(curr.left)
            if curr.right: 
                candidate.append(curr.right)
            if len(queue) == 0:
                result.append(curr.val)
                while candidate: 
                    queue.append(candidate.popleft())
                    
            
        return result
            
        