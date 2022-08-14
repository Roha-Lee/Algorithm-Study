/**
 * // Definition for a Node.
 * function Node(val, children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node|null} root
 * @return {number[]}
 */
 var preorder = function(root) {
    let result = [];
    helper(root, result);
    return result;
};

const helper = function(node, result) {
    if (node === null) return;
    result.push(node.val);
    for (let child of node.children) {
        helper(child, result);
    }
}