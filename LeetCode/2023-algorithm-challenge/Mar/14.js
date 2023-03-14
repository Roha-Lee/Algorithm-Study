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
 * @return {number}
 */
var sumNumbers = function(root) {
    // dfs로 돌면서 모든 수 구하기 
    const numbers = [];
    const dfs = (node, temp = []) => {
        if (node.left === null && node.right === null) {
            temp.push(String(node.val));
            numbers.push(parseInt(temp.join(""), 10));
            temp.pop();
            return;
        }
        if (node.left !== null) {
            temp.push(String(node.val));
            dfs(node.left, temp);
            temp.pop();
        }
        if (node.right !== null) {
            temp.push(String(node.val));
            dfs(node.right, temp);
            temp.pop();
        }
    };
    dfs(root);
    return numbers.reduce((acc, cur) => acc + cur, 0);
};
