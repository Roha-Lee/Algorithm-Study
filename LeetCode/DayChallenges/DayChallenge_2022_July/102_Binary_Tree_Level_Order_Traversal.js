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
 * @return {number[][]}
 */
 var levelOrder = function(root) {
  const result = [];
  const traverse = function(node, result, depth) {
      if (node === null) return;
      if (result.length === depth) {
          result.push([]);
      }
      traverse(node.left, result, depth+1);
      traverse(node.right, result, depth+1);
      result[depth].push(node.val);
  }
  traverse(root, result, 0);
  return result;
};
