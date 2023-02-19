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
var zigzagLevelOrder = function(root) {
    if (!root) {
        return [];
    }
    let queue = [root];
    let nextQueue = [];
    let result = [];
    let temp = [];
    let direction = false;
    while (queue.length) {
        for (let i = 0; i < queue.length; i += 1) {
            const cur = queue[i];
            temp.push(cur.val);
            if (cur.left) nextQueue.push(cur.left);
            if (cur.right) nextQueue.push(cur.right);
        }
        queue = nextQueue;
        nextQueue = [];
        if (direction) {
            temp.reverse();
            result.push(temp);
        } else {
            result.push(temp);
        }
        direction = !direction;
        temp = [];
    }
    return result;
};
