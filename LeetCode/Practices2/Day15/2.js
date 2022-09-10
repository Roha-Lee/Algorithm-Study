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
 var isSymmetric = function(root) {
    if (root === null) return true;
    const checkSymmetric = function(leftSide, rightSide) {
        if (leftSide === null && rightSide === null) return true;
        else if(leftSide !== null && rightSide !== null) {
            if (leftSide.val !== rightSide.val) return false;
            else {
                return checkSymmetric(leftSide.left, rightSide.right) && 
                       checkSymmetric(leftSide.right, rightSide.left);
            }
        } else return false;
    }
    return checkSymmetric(root.left, root.right);
};

