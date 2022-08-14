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
    if (root === null) return [];
    let result = [];
    let curr; 
    let nextQ = [];
    let q = [root];
    while(q.length) {
        const temp = [];
        while(q.length) {
            curr = q.shift();
            temp.push(curr.val);
            if (curr.left) nextQ.push(curr.left);
            if (curr.right) nextQ.push(curr.right);    
        }
        result.push(temp);
        q = nextQ;
        nextQ = [];
    }
    return result;
};