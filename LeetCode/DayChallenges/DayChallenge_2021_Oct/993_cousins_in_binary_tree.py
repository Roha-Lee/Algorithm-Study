# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_depth_and_parent(self, depth, prev_node, curr_node, node1, node2, results):
        if curr_node is None: 
            return 
        if curr_node.val == node1 or curr_node.val == node2:
            val = None if prev_node is None else prev_node.val
            results.append((depth, val))
        self.get_depth_and_parent(depth + 1, curr_node, curr_node.left, node1, node2, results)
        self.get_depth_and_parent(depth + 1, curr_node, curr_node.right, node1, node2, results)
        
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        results = []
        self.get_depth_and_parent(0, None, root, x, y, results)
        if results[0][0] == results[1][0] and results[0][1] != results[1][1]:
            return True
        return False