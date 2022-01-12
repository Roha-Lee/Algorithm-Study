class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        curr = root
        while curr:
            if curr.val < val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    return root
            else:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    return root
        