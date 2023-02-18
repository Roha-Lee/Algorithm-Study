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
 * @return {TreeNode}
 */
var invertTree = function(root) {
    if (root) invert(root);
    return root;
};

var invert = function(node) {
    if (!node.left && !node.right) return;
    const temp = node.left;
    node.left = node.right;
    node.right = temp;
    if (node.left) invert(node.left);
    if (node.right) invert(node.right);
}
