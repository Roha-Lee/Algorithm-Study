# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, result, results):
        if node.left is None and node.right is None:
            result.append(node)
            results.append([str(node.val) for node in result])
            result.pop()
            return 
        if node.left:
            result.append(node)
            self.dfs(node.left, result, results)
            result.pop()
        if node.right:
            result.append(node)
            self.dfs(node.right, result, results)
            result.pop()
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        results = []
        self.dfs(root, [], results)
        total = 0
        for result in results:
            total += int(''.join(result))
        return total