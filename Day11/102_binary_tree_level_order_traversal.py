# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Queue:
    def __init__(self):
        self.data = []
    def push(self, x):
        return self.data.append(x)
    def pop(self):
        if self.data:
            return self.data.pop(0)
    def __len__(self):
        return len(self.data)
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return 
        
        result = []
        depth_result = []
        prev_depth = curr_depth = 0
        queue = Queue()
        curr = root
        
        while curr:
            if curr.left: queue.push((curr_depth+1, curr.left))
            if curr.right: queue.push((curr_depth+1, curr.right))
            
            depth_result.append(curr.val)
            prev_depth = curr_depth    
            
            if len(queue) == 0:
                curr = None
                curr_depth += 1
            else:
                (curr_depth, curr) = queue.pop()
            
            if curr_depth != prev_depth:
                result.append(depth_result)
                depth_result = []
                
        return result

# Recursive solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def _traverse(result, node, depth):
            if node is None: return 
            if len(result) == depth:
                result.append([])
            _traverse(result, node.left, depth + 1)
            _traverse(result, node.right, depth + 1)
            result[depth].append(node.val)
        _traverse(result, root, 0)
        return result