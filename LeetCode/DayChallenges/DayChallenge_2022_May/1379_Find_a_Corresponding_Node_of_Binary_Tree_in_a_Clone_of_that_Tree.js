/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} node
 * @param {number} target
 * @return {TreeNode}
 */
 const findTargetFromTree = function(node, target) {
    let result;
    if(node === null) return null;
    if(node.val === target) return node;
    if(node.left) {
        result ||= findTargetFromTree(node.left, target);
    }
    if(node.right) {
        result ||= findTargetFromTree(node.right, target);
    }
    return result;
}


/**
 * @param {TreeNode} original
 * @param {TreeNode} cloned
 * @param {TreeNode} target
 * @return {TreeNode}
 */
var getTargetCopy = function(original, cloned, target) {
    return findTargetFromTree(cloned, target.val);
};