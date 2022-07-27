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
 * @return {void} Do not return anything, modify root in-place instead.
 */
 var flatten = function(root) {
    let nextOne = null;
    const update = node => {
        if (!node) return node;
        
        update(node.right);
        update(node.left);
        node.right = nextOne;
        node.left = null;
        nextOne = node;   
    }
    update(root);
};

