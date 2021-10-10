# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct_tree(self, inorder, parent, preorder):
        if len(preorder) == 0:
            return
        
        if len(preorder) == 1:
            curr = preorder.pop(0)
            node = TreeNode(curr)    
            return node
        
        curr = preorder.pop(0)
        node = TreeNode(curr)    
        
        index = -1
        for i in range(len(inorder)):
            if inorder[i] == curr:
                index = i
                break
                
        parent = node
        left = inorder[:index]
        right = inorder[index+1:]
        parent.left = self.construct_tree(left, parent, preorder[:index])
        parent.right = self.construct_tree(right, parent, preorder[index:])
        
        return parent
            
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.construct_tree(inorder, None, preorder)
    
        