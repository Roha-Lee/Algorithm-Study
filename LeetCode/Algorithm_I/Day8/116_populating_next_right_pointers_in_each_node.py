"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None: return 
        q = deque()
        cnt = 0
        level = 1
        q.append(root)
        
        node = prev = None
        while q: 
            prev = node
            node = q.popleft()
            cnt += 1 
            if cnt == 2 ** level:
                level += 1
                prev.next = None
            else:
                if cnt > 1:
                    prev.next = node
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        node.next = None
        return root