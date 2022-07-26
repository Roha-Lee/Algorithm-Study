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
    let result;
    check(root);
    return result;
    function check (node) {
        if (node === null) return false;
        const leftExist = check(node.left);
        const rightExist = check(node.right);
        const exist = q === node || p === node;
        if (leftExist || rightExist) {
            if ((leftExist && exist) || (leftExist && rightExist) || (rightExist && exist)) {
                if (!result) {
                    result = node;    
                }
            }
            return true;
        }
        if (exist) {
            return true;
        }
        return false;
    };
};

