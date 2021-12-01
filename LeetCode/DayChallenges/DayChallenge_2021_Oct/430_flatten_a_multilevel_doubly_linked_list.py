"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def dfs(self, node, result):
        if node is None: 
            return result
        stack = [node]
        while stack: 
            node = stack.pop()
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
                
            result.next = node
            node.prev = result
            result.child = None
            result = result.next
            

            
    def flatten(self, head: 'Node') -> 'Node':
        root = Node(0, None, None, None)
        self.dfs(head, root)
        ret_val = root.next
        if ret_val:
            ret_val.prev = None
        return ret_val
        
        