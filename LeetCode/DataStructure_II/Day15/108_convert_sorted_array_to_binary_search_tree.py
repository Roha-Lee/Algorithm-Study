# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def merge(self, nums, parent, direction='root'):
        if len(nums) == 0:
            return 
            
        mid = len(nums) // 2
        left, right = nums[:mid], nums[mid+1:]
        curr = TreeNode(nums[mid])
        
        if direction == 'left':
            parent.left = curr
        elif direction == 'right':
            parent.right = curr
        else:
            parent = curr

        self.merge(left, curr, 'left')
        self.merge(right, curr, 'right')
        
        return parent
    
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.merge(nums, None)
        
        