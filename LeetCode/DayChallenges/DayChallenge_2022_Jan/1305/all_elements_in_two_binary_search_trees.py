# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node, result):
            if node is None: return 
            inorder(node.left, result)
            result.append(node.val)
            inorder(node.right, result)
        res1, res2 = [], []
        inorder(root1, res1)
        inorder(root2, res2)
        
        def merge(res1, res2):
            res1, res2 = deque(res1), deque(res2)
            result = []
            while res1 and res2:
                if res1[0] < res2[0]:
                    result.append(res1.popleft())
                else:
                    result.append(res2.popleft())
            while res1:
                result.append(res1.popleft())
            while res2:
                result.append(res2.popleft())
            return result
        return merge(res1, res2)
        