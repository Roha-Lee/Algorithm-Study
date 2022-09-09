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
 * @return {number[]}
 */
 var rightSideView = function(root) {
    const result = [];
    const helper = function(node, depth) {
        if (node === null) return;
        if (depth < result.length) result[depth] = node.val;
        else result.push(node.val);
        helper(node.left, depth + 1);
        helper(node.right, depth + 1);
    }
    helper(root, 0);
    return result;
};