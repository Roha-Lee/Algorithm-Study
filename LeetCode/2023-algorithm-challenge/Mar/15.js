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
var isCompleteTree = function(root) {
    const vals = [];
    let nextQueue = [];
    let queue = [root];
    while (queue.length) {
        while (queue.length) {
            const node = queue.shift();
            vals.push(node === null ? null : node.val);
            if (node !== null) {
                nextQueue.push(node.left);
                nextQueue.push(node.right);
            }
        }
        queue = nextQueue;
        nextQueue = [];
    }
    while (vals[vals.length - 1] === null) {
        vals.pop();
    }
    return vals.reduce((acc, cur) => acc && cur !== null, true);
};
