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
 * @return {TreeNode[]}
 */
var findDuplicateSubtrees = function(root) {
    const structHash = new Map();
    const result = [];
    const inorder = (node) => {
        if (node === null || node.val === null) {
            return "";
        }
        let tag = "[";
        tag += inorder(node.left);
        tag += String(node.val);
        tag += inorder(node.right);
        tag += "]";
        const count = structHash.get(tag) || 0;
        if (count == 1) {
            result.push(node);
        }
        structHash.set(tag, count + 1);
        return tag;
    }
    inorder(root);
    return result;
};
