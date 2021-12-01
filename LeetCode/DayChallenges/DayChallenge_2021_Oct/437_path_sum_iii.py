# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def prefix_tree(self, node, curr_sum = 0):
        if node is None: return 
        curr_sum = node.val + curr_sum
        node.val = curr_sum
        self.prefix_tree(node.left, curr_sum)
        self.prefix_tree(node.right, curr_sum)
        
    def find(self, node, target_sum, targets, count = 0):
        if node is None: return count        
        count += targets.count(node.val)
        targets.append(target_sum + node.val)
        
        count = self.find(node.left, target_sum, targets, count)
        count = self.find(node.right, target_sum, targets, count)    
        
        targets.pop()
        
        return count
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.prefix_tree(root)
        return self.find(root, targetSum, [targetSum])
        