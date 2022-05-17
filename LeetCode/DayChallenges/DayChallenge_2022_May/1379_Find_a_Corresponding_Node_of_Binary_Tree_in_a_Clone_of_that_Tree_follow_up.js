/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} node
 * @param {TreeNode} clonedNode
 * @param {TreeNode} target
 * @return {TreeNode}
 */
 const findTargetFromTree = function(node, clonedNode, target) {
    if(node === null) return null;
    if(node === target) return clonedNode;
    return  findTargetFromTree(node.left, clonedNode.left, target) ||
            findTargetFromTree(node.right, clonedNode.right, target);
}


/**
 * @param {TreeNode} original
 * @param {TreeNode} cloned
 * @param {TreeNode} target
 * @return {TreeNode}
 */
var getTargetCopy = function(original, cloned, target) {
    return findTargetFromTree(original, cloned, target);
};