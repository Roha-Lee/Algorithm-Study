# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, node, remain, path, results):
        if node is None:
            return 
        
        if node.left is None and node.right is None: 
            if remain - node.val == 0:
                path.append(node.val)
                results.append(path[:])
                path.pop()
            return
        
        path.append(node.val)
        self.DFS(node.left, remain - node.val, path, results)
        self.DFS(node.right, remain - node.val, path, results)
        path.pop()
            
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        results = []
        self.DFS(root, targetSum, [], results)
        return results