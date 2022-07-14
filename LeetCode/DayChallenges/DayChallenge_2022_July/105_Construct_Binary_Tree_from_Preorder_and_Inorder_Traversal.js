/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
 var buildTree = function(preorder, inorder) {
    if(preorder.length === 0) return null;
    const root = new TreeNode(preorder[0]);
    const inorderIndex = inorder.findIndex(item => item === root.val);
    const inorderLeft = inorder.slice(0, inorderIndex);
    const inorderRight = inorder.slice(inorderIndex+1);
    const preorderLeft = preorder.slice(1, 1+inorderLeft.length);
    const preorderRight = preorder.slice(inorderLeft.length+1);  
    root.left = buildTree(preorderLeft, inorderLeft);
    root.right = buildTree(preorderRight, inorderRight);
    return root;
};