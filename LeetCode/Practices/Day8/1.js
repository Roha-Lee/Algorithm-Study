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
 * @return {boolean}
 */
 var isValidBST = function(root) {
    var helper = function(node, low=-Infinity, high=Infinity) {
        if (node === null) return true;
        if (node.val <= low || node.val >= high) return false;
        return helper(node.left, low, node.val) && helper(node.right, node.val, high);
    }
    return helper(root);
};