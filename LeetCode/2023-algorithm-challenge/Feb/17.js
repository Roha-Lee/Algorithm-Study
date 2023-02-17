/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDiffInBST = function(root) {
    const values = [];
    const inorder = (node) => {
        if (node === null) return;
        if (node.left) {
            inorder(node.left);
        }
        values.push(node.val);
        if (node.right) {
            inorder(node.right);
        }
    }
    inorder(root);
    values.sort((a, b) => a - b);
    values.push(Infinity);
    
    let result = Infinity;
    for (let i = 1; i < values.length; i += 1) {
        result = Math.min(values[i] - values[i-1], result);
    }
    return result;
};
