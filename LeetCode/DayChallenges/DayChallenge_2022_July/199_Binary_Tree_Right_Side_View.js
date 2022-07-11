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
  if (root === null) return [];
  const result = new Array(root.length);
  inorder(root, 0, result);
  return result;
};

const inorder = function(node, depth, arr) {
  if(node.left) inorder(node.left, depth + 1, arr);
  arr[depth] = node.val;
  if(node.right) inorder(node.right, depth + 1, arr);
}