class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traversal(node, result):
            if node is None: return 
            result.append(node.val)
            traversal(node.left, result)
            traversal(node.right, result)
            return result
        
        if root is None: return True
        
        left_nodes = []
        right_nodes = []
        traversal(root.left, left_nodes)
        traversal(root.right, right_nodes)
        for node_val in left_nodes:
            if root.val <= node_val:
                return False
        for node_val in right_nodes:
            if root.val >= node_val:
                return False
            
        valid_left = self.isValidBST(root.left)
        valid_right = self.isValidBST(root.right)
        
        return valid_left and valid_right
            