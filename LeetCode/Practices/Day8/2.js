/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
 var lowestCommonAncestor = function(root, p, q) {
    let node;
    var helper = function(curr) {
        if (curr === null) return false;
        const count = helper(curr.left) + helper(curr.right) + (curr === p) + (curr === q);
        if (count > 0) {
            if (!node && count === 2) node = curr;
            return true;
        }
        return false;
    };    
    helper(root);
    return node;
};
