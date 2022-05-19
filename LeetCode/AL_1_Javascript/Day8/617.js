/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {TreeNode}
 */
 const mergeTrees = function(root1, root2) {
    if(!root1 && !root2) return null;
    const val1 = root1? root1.val : 0;
    const val2 = root2? root2.val : 0;
    const merged = new TreeNode(val1 + val2);
    merged.left = mergeTrees(root1?.left, root2?.left);
    merged.right = mergeTrees(root1?.right, root2?.right);
    return merged;
};