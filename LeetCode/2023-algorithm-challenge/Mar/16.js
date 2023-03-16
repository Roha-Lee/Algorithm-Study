/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function(inorder, postorder) {
    const curLen = inorder.length;
    if (curLen === 0) {
        return null;
    }
    const centerVal = postorder[curLen - 1];
    const inorderCenter = inorder.findIndex(item => item === centerVal);
    return new TreeNode(
        centerVal, 
        buildTree(inorder.slice(0, inorderCenter), postorder.slice(0, inorderCenter)), 
        buildTree(inorder.slice(inorderCenter + 1), postorder.slice(inorderCenter, -1)),
    );
};
